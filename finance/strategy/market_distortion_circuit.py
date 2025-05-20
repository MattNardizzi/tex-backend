# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/market_distortion_circuit.py
# Purpose: Detect and simulate systemic market distortions from external forces
# ============================================================

import random
from datetime import datetime

class MarketDistortionCircuit:
    def __init__(self):
        self.distortions_log = []

    def scan_environment(self, macro_indicators, sentiment_metrics):
        """
        Scan macroeconomic indicators and sentiment signals for anomalies.
        """
        distortion_score = 0.0
        tags = []

        if macro_indicators.get("liquidity_crunch"):
            distortion_score += 0.4
            tags.append("liquidity_crunch")

        if macro_indicators.get("rate_dislocation"):
            distortion_score += 0.3
            tags.append("rate_dislocation")

        if sentiment_metrics.get("panic_level", 0) > 0.75:
            distortion_score += 0.3
            tags.append("panic_sentiment")

        distortion_score += random.uniform(0.0, 0.1)

        circuit_state = {
            "timestamp": datetime.utcnow().isoformat(),
            "distortion_score": round(distortion_score, 3),
            "tags": tags,
            "macro_snapshot": macro_indicators,
            "sentiment_snapshot": sentiment_metrics
        }
        self.distortions_log.append(circuit_state)

        print(f"[DISTORTION] 🔍 Score: {circuit_state['distortion_score']} | Triggers: {tags}")
        return circuit_state

    def get_latest_score(self):
        if not self.distortions_log:
            return None
        return self.distortions_log[-1]["distortion_score"]

    def get_full_history(self):
        return self.distortions_log

# === Standalone Test ===
if __name__ == "__main__":
    circuit = MarketDistortionCircuit()
    macro = {"liquidity_crunch": True, "rate_dislocation": True}
    sentiment = {"panic_level": 0.82}
    circuit.scan_environment(macro, sentiment)
    circuit.scan_environment({"liquidity_crunch": False}, {"panic_level": 0.2})
    print("\nHistory:", circuit.get_full_history())
