# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/strategy_scoring.py
# Purpose: Tier 6 — Synthetic Strategy Evaluator + Pruner
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

class StrategyScorer:
    def __init__(self):
        self.history = []

    def evaluate(self, strategy, regret_score=0.0, forecast_confidence=0.5):
        """
        Scores the synthetic strategy based on regret, coherence, and foresight projection.
        """
        tone = strategy.get("emotional_tone", "neutral")
        urgency = strategy.get("urgency", 0.7)
        coherence = strategy.get("coherence", 0.8)

        # Dynamic scoring formula (customizable)
        volatility_bias = strategy["modifiers"].get("volatility_bias", 1.0)
        stability_weight = strategy["modifiers"].get("stability_weight", 1.0)

        impact_score = round(
            (1 - regret_score) * coherence * stability_weight * forecast_confidence -
            (urgency * volatility_bias * 0.3),
            3
        )

        strategy_record = {
            "id": strategy["id"],
            "timestamp": datetime.utcnow().isoformat(),
            "score": impact_score,
            "reasoning": {
                "regret": regret_score,
                "confidence": forecast_confidence,
                "coherence": coherence,
                "tone": tone
            }
        }

        self.history.append(strategy_record)
        store_to_memory("strategy_scores", strategy_record)

        if impact_score < 0.2:
            print(f"[STRATEGY PRUNE] 🪓 Strategy {strategy['id']} marked for pruning (score: {impact_score})")
        else:
            print(f"[STRATEGY SCORE] ✅ Strategy {strategy['id']} scored: {impact_score}")

        return impact_score