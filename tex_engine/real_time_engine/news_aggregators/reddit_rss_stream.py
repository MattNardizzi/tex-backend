# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/reddit_rss_stream.py
# Purpose: Real-time Reddit RSS stream for Tex AGI awareness
# ============================================================

import feedparser
import time
import urllib.request
from datetime import datetime
from core_layer.memory_engine import store_to_memory

# === Optional Signal Fusion System ===
try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

# === Global Constants ===
SUBREDDITS = ["algotrading", "finance", "wallstreetbets", "investing", "stockmarket"]
PROCESSED_LINKS = set()
FEEDPARSER_HEADERS = {'User-Agent': 'TexAGI/1.0 (+https://vortexblack.ai)'}


def score_urgency(title):
    keywords = ["crash", "panic", "fed", "inflation", "buy", "sell", "short", "moon", "unemployment", "collapse", "dip"]
    urgency = 0.1
    for word in keywords:
        if word in title.lower():
            urgency += 0.2
    return round(min(1.0, urgency), 2)


def fetch_reddit_rss_batch(limit=15):
    results = []
    for subreddit in SUBREDDITS:
        url = f"https://www.reddit.com/r/{subreddit}/.rss"
        try:
            req = urllib.request.Request(url, headers=FEEDPARSER_HEADERS)
            feed = feedparser.parse(urllib.request.urlopen(req))
            if not feed.entries:
                print(f"[REDDIT RSS] ⚠️ No entries found for r/{subreddit}")
                continue

            for entry in feed.entries[:5]:
                if entry.link in PROCESSED_LINKS:
                    continue
                PROCESSED_LINKS.add(entry.link)

                urgency = score_urgency(entry.title)
                post = {
                    "source": "reddit_rss",
                    "subreddit": subreddit,
                    "title": entry.title,
                    "summary": getattr(entry, "summary", ""),
                    "urgency": urgency,
                    "timestamp": datetime.utcnow().isoformat(),
                    "link": entry.link
                }

                store_to_memory("tex_reddit_rss_stream", post)
                if FUSION_ENABLED:
                    register_signal(post)

                print(f"[REDDIT] 🔥 r/{subreddit} | {entry.title} (Urgency: {urgency})")
                results.append(post)

                if len(results) >= limit:
                    return results

        except Exception as e:
            print(f"[REDDIT ERROR] r/{subreddit} → {e}")

    return results


def run_reddit_stream_loop():
    print("🧠 [REDDIT RSS] Polling started.")
    while True:
        fetch_reddit_rss_batch()
        time.sleep(90)


# === ✅ Class-Based Wrapper for Tex Integration ===
class RedditRSSStream:
    def __init__(self, limit=5):
        self.limit = limit

    def fetch_posts(self):
        return fetch_reddit_rss_batch(limit=self.limit)


# === Local Test Loop ===
if __name__ == "__main__":
    run_reddit_stream_loop()