# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/forecast_engine.py
# Purpose: Generate short-term forecasts from memory archives
# ============================================================

import os
import json
from datetime import datetime, timezone, timedelta
from statistics import mean
from core_layer.memory_engine import recall_recent

def forecast_market_sentiment(agent_name="tex_newsapi_stream", window_minutes=10):
    """
    Generates a short-term market sentiment forecast 
    based on urgency values in recent memory entries.
    """
    # Pull the last ~20 memories from RAM (filtered by agent)
    recent_entries = recall_recent(n=20)

    # Filter by agent and by recency if timestamps available
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=window_minutes)
    filtered = []

    for entry in recent_entries:
        try:
            ts = datetime.fromisoformat(entry["timestamp"])
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            if ts >= cutoff and entry.get("agent") == agent_name:
                urgency = entry.get("data", {}).get("urgency", 0.5)
                filtered.append(urgency)
        except Exception as e:
            print(f"[FORECAST WARNING] ⚠️ Bad memory skipped: {e}")
            continue

    if not filtered:
        return {"prediction": "neutral", "confidence": 0.0, "avg_urgency": 0.5, "timestamp": datetime.now(timezone.utc).isoformat()}

    avg = mean(filtered)

    if avg > 0.75:
        prediction = "bullish"
    elif avg < 0.35:
        prediction = "bearish"
    else:
        prediction = "neutral"

    confidence = round(abs(avg - 0.5) * 2, 2)
    
    return {
        "prediction": prediction,
        "confidence": confidence,
        "avg_urgency": round(avg, 2),
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# === Optional CLI Debug Mode
if __name__ == "__main__":
    print("🧠 Forecasting short-term market sentiment...")
    result = forecast_market_sentiment()
    print(f"Prediction: {result['prediction']} | Confidence: {result['confidence']} | Avg Urgency: {result['avg_urgency']}")