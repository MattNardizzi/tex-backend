# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/rss_stream.py
# Purpose: Tex RSS Stream — Structured Financial & Global Awareness Engine
# ============================================================

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import feedparser
import time
import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

# Optional signal fusion
try:
    from real_time_engine.signal_fusion import register_signal
    FUSION_ENABLED = True
except ImportError:
    FUSION_ENABLED = False

class RSSStream:
    def __init__(self):
        self.feeds = [
            # Finance & Business
            "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
            "https://www.bloomberg.com/feed/podcast/etf-report.xml",
            "https://www.ft.com/?format=rss",
            "http://feeds.reuters.com/reuters/businessNews",
            "https://feeds.marketwatch.com/marketwatch/topstories/",
            "https://finance.yahoo.com/news/rssindex",
            "https://news.google.com/rss/search?q=business&hl=en-US&gl=US&ceid=US:en",
            "http://feeds.bbci.co.uk/news/business/rss.xml",

            # Crypto & Forex
            "https://cointelegraph.com/rss",
            "https://bitcoinmagazine.com/.rss/full",
            "https://www.dailyfx.com/feeds/forex-market-news",
            "https://www.forexlive.com/feed/news",
            "https://www.fxstreet.com/rss/news",

            # Commodities
            "https://oilprice.com/rss/main",
            "https://www.investing.com/rss/news_301.rss",
            "https://www.investing.com/rss/news_4.rss",
            "https://www.kitco.com/rss/",

            # Macro & Central Banks
            "https://www.weforum.org/agenda/rss.xml",
            "https://seekingalpha.com/market_currents.xml",
            "https://www.zerohedge.com/fullrss.xml",
            "https://www.imf.org/en/News/rss",
            "https://www.federalreserve.gov/feeds/press_all.xml",
        ]
        self.processed_links = set()

    def score_urgency(self, title):
        keywords = ["crash", "panic", "inflation", "fed", "buy", "sell", "bank", "default", "volatility", "recession"]
        score = 0.1
        for keyword in keywords:
            if keyword in title.lower():
                score += 0.2
        return round(min(score, 1.0), 2)

    def fetch_headlines(self):
        results = []
        for url in self.feeds:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries[:3]:
                    if entry.link in self.processed_links:
                        continue

                    self.processed_links.add(entry.link)
                    urgency = self.score_urgency(entry.title)

                    story = {
                        "source": "rss",
                        "url": url,
                        "title": entry.title,
                        "summary": getattr(entry, "summary", ""),
                        "timestamp": datetime.utcnow().isoformat(),
                        "urgency_score": urgency,
                        "sentiment": random.choice(["positive", "neutral", "negative"])
                    }

                    results.append(story)
                    store_to_memory("tex_rss_stream", story)
                    if FUSION_ENABLED:
                        register_signal(story)

                    print(f"[RSS] 📰 {entry.title} (urgency: {urgency})")
            except Exception as e:
                print(f"[RSS ERROR] {url} — {e}")
        return results

    def get_enriched_batch(self, limit=10):
        all_headlines = self.fetch_headlines()
        random.shuffle(all_headlines)
        return all_headlines[:limit]

# === Entry point for independent testing ===
def start_rss_stream_loop():
    rss = RSSStream()
    print("🧠 [RSS] Stream loop started.")
    while True:
        try:
            batch = rss.get_enriched_batch()
            for story in batch:
                print(f"[RSS] 🧠 {story['title']} | Urgency: {story['urgency_score']} | Sentiment: {story['sentiment']}")
        except Exception as e:
            print(f"[RSS LOOP ERROR] {e}")
        time.sleep(90)

if __name__ == "__main__":
    start_rss_stream_loop()