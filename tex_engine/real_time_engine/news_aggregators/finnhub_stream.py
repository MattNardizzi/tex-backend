# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/finnhub_stream.py
# Purpose: Finnhub API News Feed Integration for Tex
# ============================================================

import requests
import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv
from core_layer.memory_engine import store_to_memory

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

def fetch_finnhub_news(limit=10):
    url = f"https://finnhub.io/api/v1/news?category=general&token={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        news_items = response.json()[:limit]
        results = []

        for item in news_items:
            enriched = {
                "title": item.get("headline", ""),
                "summary": item.get("summary", ""),
                "source": "finnhub_api",
                "timestamp": datetime.utcnow().isoformat(),
                "sentiment": random.choice(["positive", "neutral", "negative"]),
                "urgency_score": round(random.uniform(0.2, 1.0), 2),
                "link": item.get("url", "")
            }
            store_to_memory("tex_finnhub_stream", enriched)
            results.append(enriched)
            print(f"[FINNHUB] 📰 {enriched['title']} (Urgency: {enriched['urgency_score']})")

        return results

    except Exception as e:
        print(f"[FINNHUB API ERROR] {e}")
        return []

def fetch_finnhub_news_loop(limit=10):
    print("🧠 [FINNHUB STREAM] Polling loop started.")
    while True:
        fetch_finnhub_news(limit=limit)
        time.sleep(90)

if __name__ == "__main__":
    fetch_finnhub_news_loop()