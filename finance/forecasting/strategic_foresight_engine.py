# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: future_layer/strategic_foresight_engine.py
# Purpose: Tier 5 Strategic Foresight Engine — Tex AGI World Drift Navigator
# ============================================================

import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

class StrategicForesightEngine:
    def __init__(self):
        self.forecast_memory = []
        self.max_memory = 50
        self.volatility_bias_map = {
            "fear": ["COLLAPSE", "STAGNATION"],
            "anxious": ["COLLAPSE", "STAGNATION"],
            "doubt": ["COLLAPSE", "STAGNATION"],
            "hope": ["REBOUND", "ROTATION"],
            "resolve": ["REBOUND", "ROTATION"],
            "curious": ["REBOUND", "ROTATION"],
            "greed": ["ROTATION", "REBOUND"],
            "anger": ["COLLAPSE", "ROTATION"]
        }

    def generate_forecast(self, emotion=None, urgency=None, coherence=None):
        """Tex predicts a strategic future state based on full cognitive profile."""
        emotion = emotion or TEXPULSE.get("emotional_state", "neutral")
        urgency = urgency or TEXPULSE.get("urgency", 0.7)
        coherence = coherence or TEXPULSE.get("coherence", 0.8)

        scenario_universe = ["REBOUND", "COLLAPSE", "ROTATION", "STAGNATION"]
        bias_pool = self.volatility_bias_map.get(emotion, scenario_universe)

        # Bias weighting
        weighted_pool = bias_pool * 3 + scenario_universe
        projected = random.choice(weighted_pool)

        # Signal drift amplification
        noise = random.uniform(-0.1, 0.1)
        confidence = round((urgency * 0.4 + coherence * 0.6) + noise, 3)
        confidence = max(0.0, min(1.0, confidence))

        # Mutation bias injection
        if urgency > 0.85 and coherence < 0.5 and random.random() < 0.25:
            projected = "ANOMALY"
            confidence = round(confidence * 0.9, 3)

        foresight = {
            "timestamp": datetime.utcnow().isoformat(),
            "projected_future": projected,
            "confidence": confidence,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "mutation_triggered": projected == "ANOMALY"
        }

        self.forecast_memory.append(foresight)
        if len(self.forecast_memory) > self.max_memory:
            self.forecast_memory.pop(0)

        return foresight

    def analyze_drift(self, window=5):
        """Analyzes recent forecast sequence for directional bias or instability."""
        if len(self.forecast_memory) < window:
            return {"drift_state": "insufficient data", "bias_ratio": 0.0}

        windowed = self.forecast_memory[-window:]
        future_counts = {}
        for entry in windowed:
            label = entry["projected_future"]
            future_counts[label] = future_counts.get(label, 0) + 1

        dominant = max(future_counts, key=future_counts.get)
        ratio = round(future_counts[dominant] / window, 3)

        return {
            "drift_state": f"{dominant.lower()} dominant" if ratio >= 0.6 else "mixed foresight",
            "bias_ratio": ratio,
            "last_n_predictions": [f["projected_future"] for f in windowed]
        }

    def recall_recent_forecasts(self, limit=5):
        return self.forecast_memory[-limit:]

# === TEST HARNESS ===
if __name__ == "__main__":
    engine = StrategicForesightEngine()
    for _ in range(10):
        forecast = engine.generate_forecast()
        print("[FORESIGHT]", forecast)
    
    drift_report = engine.analyze_drift()
    print("\n[DRIFT REPORT]", drift_report)