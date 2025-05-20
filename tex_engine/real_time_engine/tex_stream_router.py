# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/tex_stream_router.py
# Purpose: Unified Stream Launcher for Real-Time Awareness
# ============================================================

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import threading
import time

from news_aggregators.rss_stream import RSSStream
from news_aggregators.reddit_rss_stream import fetch_reddit_rss_batch
from news_aggregators.finnhub_stream import fetch_finnhub_news_loop
from polygon_stream import start_polygon_stream

rss_data = []
reddit_data = []
finnhub_data = []
polygon_thread = None


def launch_rss_stream():
    print("[✅ RSS STREAM STARTED]")
    rss = RSSStream()
    global rss_data
    while True:
        try:
            rss_data = rss.get_enriched_batch(limit=5)
            for item in rss_data:
                print(f"[RSS] 🧠 {item['title']} | Sentiment: {item.get('sentiment')} | Urgency: {item.get('urgency_score')}")
        except Exception as e:
            print(f"[RSS ERROR] {e}")
        time.sleep(90)


def launch_reddit_stream():
    print("[✅ REDDIT STREAM STARTED]")
    global reddit_data
    while True:
        try:
            reddit_data = fetch_reddit_rss_batch(limit=5)
            if not reddit_data:
                print("[REDDIT STREAM] No posts fetched.")
            for item in reddit_data:
                print(f"[REDDIT] 🔥 {item['title']} | Urgency: {item.get('urgency')} | Subreddit: {item.get('subreddit')}")
        except Exception as e:
            print(f"[REDDIT ERROR] {e}")
        time.sleep(90)


def launch_finnhub_stream():
    print("[✅ FINNHUB STREAM STARTED]")
    global finnhub_data
    while True:
        try:
            finnhub_data = fetch_finnhub_news_loop(limit=5)
            if not finnhub_data:
                print("[FINNHUB STREAM] No news received.")
            for item in finnhub_data:
                print(f"[FINNHUB] 📰 {item['title']} | Sentiment: {item.get('sentiment')} | Urgency: {item.get('urgency_score')}")
        except Exception as e:
            print(f"[FINNHUB ERROR] {e}")
        time.sleep(120)


def launch_polygon_stream():
    print("[✅ POLYGON STREAM STARTED]")
    global polygon_thread
    try:
        polygon_thread = threading.Thread(target=start_polygon_stream)
        polygon_thread.daemon = True
        polygon_thread.start()
    except Exception as e:
        print(f"[POLYGON ERROR] {e}")


def run_all_streams():
    print("[TEX STREAM ROUTER] 🚦 Launching real-time data streams...")

    threads = [
        threading.Thread(target=launch_rss_stream),
        threading.Thread(target=launch_reddit_stream),
        threading.Thread(target=launch_finnhub_stream),
        threading.Thread(target=launch_polygon_stream),
    ]

    for t in threads:
        t.daemon = True
        t.start()

    while True:
        time.sleep(300)

if __name__ == "__main__":
    run_all_streams()