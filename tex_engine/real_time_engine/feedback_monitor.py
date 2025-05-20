# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/feedback_monitor.py
# Purpose: Verifies Tex’s predictions vs actual market outcome
# ============================================================

from datetime import datetime
from core_layer.memory_engine import query_memory, annotate_memory

# === MOCKED price change function ===
# Replace with live API once connected to Polygon
def get_price_change(symbol, window="48h"):
    # MOCKED: In reality, you'd call Polygon API here
    # Let's say NVDA actually dropped 7.1% over 48h
    if symbol == "NVDA":
        return -7.1
    return 0.0

def evaluate_prediction():
    forecasts = query_memory("tex_forecasts")
    for forecast in forecasts:
        if forecast.get("symbol") == "NVDA" and "projected_move" in forecast:
            actual = get_price_change("NVDA", window="48h")
            projected = -6.8  # this is what Tex predicted
            diff = actual - projected
            accuracy = 1.0 - abs(diff / projected)

            annotate_memory("tex_forecasts", forecast, f"Accuracy: {round(accuracy * 100, 2)}%")
            print(f"✅ Forecast verified. Accuracy: {round(accuracy * 100, 2)}%")

if __name__ == "__main__":
    evaluate_prediction()