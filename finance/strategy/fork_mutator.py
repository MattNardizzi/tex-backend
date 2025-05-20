# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/fork_mutator.py
# Purpose: AGI Recursive Fork Mutation Engine — Tex Alpha Evolution Layer
# ============================================================

import random
import copy
from datetime import datetime

class ForkMutator:
    def __init__(self, mutation_strength=0.05):
        self.mutation_strength = mutation_strength

    def mutate_strategies(self, strategy, market_mood, foresight_confidence):
        base_weights = strategy.get("weights", {})
        variants = []

        for i in range(3):
            mutated = copy.deepcopy(base_weights)
            for asset in mutated:
                mutation = random.uniform(-self.mutation_strength, self.mutation_strength)
                mood_bias = self._mood_bias_factor(market_mood)
                mutated[asset] = max(0.0, min(1.0, mutated[asset] + mutation + mood_bias))

            total = sum(mutated.values()) or 1.0
            for asset in mutated:
                mutated[asset] = round(mutated[asset] / total, 4)

            variants.append({
                "id": f"variant_{i+1}",
                "weights": mutated,
                "mutation_bias": round(mood_bias, 4),
                "timestamp": datetime.utcnow().isoformat()
            })

        return variants

    def select_dominant(self, variants, regret_score):
        regret_weight = [abs(sum(v['weights'].values()) - 1.0) + (random.random() * regret_score) for v in variants]
        best_index = regret_weight.index(min(regret_weight))
        return variants[best_index], regret_weight

    def _mood_bias_factor(self, mood):
        mood_map = {
            "fear": -0.03,
            "greed": 0.02,
            "neutral": 0.0,
            "uncertain": -0.01,
            "confident": 0.01
        }
        return mood_map.get(mood.lower(), 0.0)