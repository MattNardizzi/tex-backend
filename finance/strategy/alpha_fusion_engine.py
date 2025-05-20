# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/alpha_fusion_engine.py
# Purpose: Tier 12.5 — Fusion of Competing Alpha Signals for AGI Portfolio Confidence
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

class AlphaFusionEngine:
    def __init__(self):
        self.weights = {
            "strategy_variant": 0.4,
            "foresight": 0.35,
            "market_mood": 0.25
        }

    def fuse_alpha_signals(self, variant_alpha, foresight_signal, mood_signal):
        """
        Takes:
        - variant_alpha: dict from strategy variant simulator (e.g., coherence/confidence)
        - foresight_signal: dict from foresight (e.g., confidence/projection)
        - mood_signal: dict from market_mood_sensor (e.g., mood + strength)
        """
        confidence = (
            self.weights["strategy_variant"] * variant_alpha.get("coherence", 0.5)
            + self.weights["foresight"] * foresight_signal.get("confidence", 0.5)
            + self.weights["market_mood"] * mood_signal.get("strength", 0.5)
        )

        bias_reasoning = []
        if mood_signal["mood"] in ["fear", "euphoria"]:
            bias_reasoning.append(f"Market sentiment is {mood_signal['mood']}")
        if foresight_signal["confidence"] < 0.5:
            bias_reasoning.append("Strategic foresight indicates high uncertainty")
        if variant_alpha.get("regret", 0.0) > 0.6:
            bias_reasoning.append("Recent strategy regret is elevated")

        result = {
            "fused_confidence": round(confidence, 3),
            "bias_rationale": bias_reasoning,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Log result
        store_to_memory("alpha_fusion_output", result)
        return result

# === Test Harness ===
if __name__ == "__main__":
    fusion = AlphaFusionEngine()
    fused = fusion.fuse_alpha_signals(
        variant_alpha={"coherence": 0.72, "regret": 0.63},
        foresight_signal={"confidence": 0.44},
        mood_signal={"mood": "fear", "strength": 0.78}
    )
    print("\n[FUSED ALPHA SIGNAL]", fused)