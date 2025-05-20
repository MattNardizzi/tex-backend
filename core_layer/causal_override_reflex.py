# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/causal_override_reflex.py
# Purpose: Strategic AGI Long-Horizon Override System — Prevents Self-Destructive Alpha
# ============================================================

from datetime import datetime

class CausalOverrideReflex:
    def __init__(self, regret_threshold=0.65, foresight_weight=0.7, drift_tolerance=0.3):
        self.regret_threshold = regret_threshold
        self.foresight_weight = foresight_weight
        self.drift_tolerance = drift_tolerance

    def evaluate(self, forecast, memory_trajectory, regret, drift_score):
        try:
            confidence = forecast.get("confidence", 0.5)
            projected_path = forecast.get("projected_future", "uncertain")
            emotional_drift = memory_trajectory.get("emotional_drift", 0.0)
            coherence = memory_trajectory.get("coherence", 0.6)

            # === Core Logic
            foresight_signal = confidence * self.foresight_weight
            instability = abs(coherence - emotional_drift)

            override_score = (regret * 0.5) + (drift_score * 0.3) + (instability * 0.2)

            if override_score >= self.regret_threshold and foresight_signal < 0.55:
                return {
                    "override_triggered": True,
                    "score": round(override_score, 4),
                    "reason": "High regret with low foresight and emotional instability",
                    "timestamp": datetime.utcnow().isoformat(),
                    "projected_path": projected_path,
                    "confidence": confidence,
                    "drift": emotional_drift,
                    "coherence": coherence
                }
            else:
                return {
                    "override_triggered": False,
                    "score": round(override_score, 4),
                    "timestamp": datetime.utcnow().isoformat(),
                    "projected_path": projected_path,
                    "confidence": confidence
                }
        except Exception as e:
            return {
                "override_triggered": False,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }

    def evaluate_long_term_causality(self, forecast, memory_trajectory, regret, drift_score):
        return self.evaluate(forecast, memory_trajectory, regret, drift_score)