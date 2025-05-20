# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/sentiment/emotional_liquidity_engine.py
# Purpose: Tier 13.5 – Emotion-Driven Liquidity Adjustment Engine
# ============================================================

import math
from statistics import mean
from datetime import datetime
from core_layer.memory_engine import store_to_memory

class EmotionalLiquidityEngine:
    def __init__(self):
        self.volatility_bias = {
            "fear": 0.65,
            "greed": 1.25,
            "hope": 1.1,
            "resolve": 0.95,
            "doubt": 0.85,
            "euphoria": 1.35,
            "panic": 0.5
        }

    def adjust_portfolio(self, emotion, urgency, coherence, portfolio):
        factor = self._calculate_adjustment_factor(emotion, urgency, coherence)
        adjusted = self._apply_bias(portfolio, factor)
        self._log_adjustment(emotion, urgency, coherence, factor, portfolio, adjusted)
        return adjusted

    def _calculate_adjustment_factor(self, emotion, urgency, coherence):
        base = self.volatility_bias.get(emotion, 1.0)
        urgency_boost = 1 + (urgency - 0.5) * 0.4  # ranges ~[0.8, 1.2]
        coherence_scaler = 1 - ((1 - coherence) * 0.25)  # ranges ~[0.75, 1.0]
        return round(base * urgency_boost * coherence_scaler, 3)

    def _apply_bias(self, portfolio, factor):
        if not portfolio:
            return []

        # ✅ Handle structured portfolio with asset list
        if isinstance(portfolio, dict) and "assets" in portfolio:
            assets = portfolio["assets"]
            count = max(1, math.ceil(len(assets) * min(factor, 2.0)))
            portfolio["assets"] = assets[:count]
            return portfolio

        # ✅ Fallback: return unchanged if format is unexpected
        return portfolio

    def _log_adjustment(self, emotion, urgency, coherence, factor, original, adjusted):
        store_to_memory("emotional_liquidity_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "adjustment_factor": factor,
            "original_portfolio_size": len(original),
            "adjusted_portfolio_size": len(adjusted),
            "adjusted_assets": adjusted
        })