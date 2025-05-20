# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC
# File: finance/strategy/strategy_variant_simulator.py
# Purpose: Simulate parallel strategy variants + rank for execution
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

class StrategyVariantSimulator:
    def __init__(self, num_variants=5):
        self.num_variants = num_variants

    def simulate_variants(self, futures, foresight_confidence):
        variants = []
        for i in range(self.num_variants):
            variant = {
                "id": f"variant_{i+1}",
                "allocation": self._random_portfolio(futures),
                "coherence": round(random.uniform(0.5, 1.0), 3),
                "volatility": round(random.uniform(0.1, 0.5), 3),
                "confidence": foresight_confidence + random.uniform(-0.1, 0.1),
                "regret": round(random.uniform(0.0, 1.0), 3)
            }
            variants.append(variant)
        return variants

    def rank_variants(self, variants):
        scored = sorted(variants, key=lambda v: (v["regret"], -v["coherence"], -v["confidence"]))
        top = scored[0]
        store_to_memory("top_strategy_variant", {
            "timestamp": datetime.utcnow().isoformat(),
            "top_variant": top
        })
        return top

    def _random_portfolio(self, futures):
        return random.sample(futures, min(3, len(futures)))