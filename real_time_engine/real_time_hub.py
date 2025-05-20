# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: real_time_engine/real_time_hub.py
# Purpose: Master coordinator for launching all real-time streams + fusion
# ===========================================================

import threading
import time
from loguru import logger

# === Signal feeds ===
from real_time_engine.polygon_stream import start_polygon_stream
from real_time_engine.news_aggregators.rss_stream import start_rss_stream
from real_time_engine.news_aggregators.newsapi_stream import start_newsapi_stream
from real_time_engine.news_aggregators.twitter_stream import start_twitter_stream
from real_time_engine.news_aggregators.reddit_rss_stream import poll_rss

# === Signal merger ===
from real_time_engine.signal_fusion import run_fusion_cycle

# === Utility: Launch thread
def start_thread(target, name):
    t = threading.Thread(target=target, name=name, daemon=True)
    t.start()
    logger.info(f"[🚀] Thread launched: {name}")
    return t

# === Fusion loop runs every 30s
def fusion_loop():
    while True:
        run_fusion_cycle()
        time.sleep(30)

# === Launch everything
def start_all_streams():
    logger.info("[⚡] Launching real-time sensory cortex for Tex...")

    start_thread(poll_rss, "RedditRSS")
    start_thread(start_rss_stream, "RSS Feed")
    start_thread(start_newsapi_stream, "NewsAPI")
    start_thread(start_twitter_stream, "Twitter")
    start_thread(start_polygon_stream, "Polygon")
    start_thread(fusion_loop, "SignalFusion")

    logger.info("✅ All signal threads launched.")

    while True:
        time.sleep(5)

# === Entry point
if __name__ == "__main__":
    start_all_streams()