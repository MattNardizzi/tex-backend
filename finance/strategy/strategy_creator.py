# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/strategy_creator.py
# Purpose: Tier 6 – Autonomous Financial Strategy Generator
# ============================================================

import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

class StrategyCreator:
    def __init__(self):
        self.library = []

    def generate_strategy(self, foresight=None, regret_score=0.0):
        """
        Synthesizes a novel trade strategy using emotion, regret, and foresight projection.
        """
        tone = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.75)
        coherence = TEXPULSE.get("coherence", 0.85)
        timestamp = datetime.utcnow().isoformat()

        archetype = self._select_archetype(tone, regret_score)
        modifiers = self._generate_modifiers(foresight, urgency, coherence)

        strategy = {
            "id": f"STRAT-{random.randint(1000, 9999)}",
            "timestamp": timestamp,
            "emotional_tone": tone,
            "urgency": urgency,
            "coherence": coherence,
            "archetype": archetype,
            "modifiers": modifiers,
            "source": "TexSynthetic",
        }

        self.library.append(strategy)
        store_to_memory("synthetic_strategies", strategy)
        print(f"[STRATEGY_CREATOR] 🧠 New strategy synthesized → {strategy['id']} ({archetype})")

        return strategy

    def _select_archetype(self, tone, regret_score):
        """
        Picks base strategy archetype based on emotional tone and regret feedback.
        """
        if regret_score > 0.75:
            return "ReversalContrarian"
        if tone == "resolve":
            return "MomentumBreakout"
        if tone == "fear":
            return "LiquidityDefense"
        if tone == "greed":
            return "VolatilityHarvest"
        return "BalancedFlow"

    def _generate_modifiers(self, foresight, urgency, coherence):
        """
        Creates unique modifiers from emotional state + foresight inputs.
        """
        modifiers = {
            "volatility_bias": round(urgency * random.uniform(0.8, 1.2), 3),
            "stability_weight": round(coherence * random.uniform(0.8, 1.2), 3),
            "foresight_tag": foresight["projected_future"] if foresight else "none"
        }
        return modifiers