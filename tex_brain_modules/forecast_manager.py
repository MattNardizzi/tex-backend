# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/forecast_manager.py
# Purpose: Tex Forecast Manager — Pure Procedural Market Forecasting + World Model Drift Correction
# ============================================================

import random
import os
import json
from datetime import datetime, timezone

from core_layer.forecast_engine import forecast_market_sentiment
from core_layer.memory_engine import store_to_memory
from evolution_layer.world_model_mutator import assess_world_model_drift

def run_forecast_cycle(coherence):
    forecast = forecast_market_sentiment()
    print(f"\n🏋️ [FORECAST] {forecast['prediction']} | Confidence: {forecast['confidence']}")

    if forecast["confidence"] > 0.6:
        store_to_memory("tex_forecast_reflection", forecast)
        
    

    real_world_outcome = "neutral"
    world_log = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "forecast_engine",
        "prediction": forecast.get("prediction", "unknown"),
        "actual": real_world_outcome,
        "confidence": forecast.get("confidence", 0.0),
        "emotion": "neutral"
    }
    try:
        with open("memory_archive/world_model_log.jsonl", "a") as f:
            f.write(json.dumps(world_log) + "\n")
    except Exception as e:
        print(f"[❌ WORLD MODEL LOGGING ERROR] {e}")

    assess_world_model_drift()
