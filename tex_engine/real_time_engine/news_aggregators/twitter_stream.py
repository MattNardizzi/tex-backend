# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/news_aggregators/twitter_stream.py
# Purpose: Simulated Tweet Sentiment Stream for Tex's Signal Engine
# ============================================================

import random
import time
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from real_time_engine.signal_fusion import register_signal

MOCK_TOPICS = [
    "Federal Reserve policy",
    "AI stock surge",
    "Inflation risk",
    "Tech layoffs",
    "Oil prices spike",
    "Crypto regulations incoming",
    "Unemployment ticking up",
    "Earnings season begins",
    "Soft landing vs. stagflation",
    "China GDP shocks market"
]

SENTIMENTS = ["positive", "negative", "neutral"]

def generate_mock_tweets():
    tweets = []
    for _ in range(3):
        tweets.append({
            "text": random.choice(MOCK_TOPICS),
            "sentiment": random.choice(SENTIMENTS),
            "urgency": round(random.uniform(0.3, 1.0), 2)
        })
    return tweets

def start_twitter_stream():
    print("[TWITTER] 🧠 Simulated Twitter stream activated...")

    while True:
        tweets = generate_mock_tweets()

        for tweet in tweets:
            signal = {
                "type": "signal",
                "source": "twitter",
                "title": tweet["text"],
                "sentiment": tweet["sentiment"],
                "urgency": tweet["urgency"],
                "timestamp": datetime.utcnow().isoformat()
            }

            print(f"📥 [TWITTER] {tweet['text']} | Sentiment: {tweet['sentiment']} | Urgency: {tweet['urgency']}")
            store_to_memory("tex_twitter_stream", signal)
            register_signal(signal)

        time.sleep(12)