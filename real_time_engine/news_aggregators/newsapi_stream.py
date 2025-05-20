# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/newsapi_stream.py
# Purpose: Simulated NewsAPI signal source for financial cognition
# ============================================================

import time
import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from real_time_engine.signal_fusion import register_signal

mock_headlines = [
    "Fed to Maintain Rates Amid Market Volatility",
    "S&P 500 Surges on Tech Rally",
    "Gold Prices Dip as Dollar Strengthens",
    "Crypto Markets Show Signs of Recovery",
    "Bond Yields Hit 3-Month Highs",
    "Unemployment Claims Spike Unexpectedly",
    "JP Morgan Reports Record Earnings",
    "Tesla Announces AI Division Spin-off",
    "Apple to Enter Crypto Market in 2025"
]

def fetch_mock_news():
    return [{
        "headline": random.choice(mock_headlines),
        "impact_score": round(random.uniform(0.1, 1.0), 2)
    } for _ in range(3)]

def start_newsapi_stream():
    print("[NEWSAPI] 🧠 Simulated NewsAPI stream activated...")

    while True:
        news_batch = fetch_mock_news()

        for article in news_batch:
            signal = {
                "type": "signal",
                "source": "newsapi",
                "title": article["headline"],
                "timestamp": datetime.utcnow().isoformat(),
                "urgency": article["impact_score"]
            }

            print(f"📥 [NEWSAPI] {article['headline']} (urgency: {article['impact_score']})")
            store_to_memory("tex_newsapi_stream", signal)
            register_signal(signal)

        time.sleep(12)  # simulate delay