# ============================================================
# © 2025 VortexBlack LLC – Market Mood Sensor
# File: finance/sentiment/market_mood_sensor.py
# Purpose: Injects ambient mood into Tex's strategic layers
# ============================================================

import random

def get_market_mood():
    """
    Simulates market-wide emotional sentiment.
    Could be wired into real NLP news signals or Twitter.
    """
    mood = random.choices(
        ["euphoria", "fear", "neutral", "greed", "doubt"],
        weights=[0.1, 0.2, 0.4, 0.2, 0.1]
    )[0]
    strength = round(random.uniform(0.3, 1.0), 2)
    return {"mood": mood, "strength": strength}