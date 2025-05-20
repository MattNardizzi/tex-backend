# ============================================================
# 🔑 VortexBlack Confidential
# File: portfolio_thinker.py
# Purpose: Tier 5 AGI Portfolio Allocation Strategist (Tex Fusion Core)
# Author: Matthew Nardizzi / VortexBlack LLC
# ============================================================

import random
import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from finance.memory.future_memory import FutureMemory
from core_layer.memory_engine import recall_all
from tex_children.aeondelta import get_swarm_emotion_distribution

class PortfolioThinker:
    def __init__(self):
        self.memory = FutureMemory()
        self.swarm_emotion_state = get_swarm_emotion_distribution
        self.strategy_log = []

    def generate_allocation(self):
        """
        Tex generates dynamic allocation strategy based on:
        - AGI memory fusion
        - Emotion + urgency drift
        - Swarm emotional distribution
        - Recent future predictions
        - Goal alignment
        """
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.7)
        goals = get_active_goals()
        futures = self.memory.list_predicted_futures(realized=False)
        swarm_bias = self.swarm_emotion_state()

        weights = {
            "equities": 0.25,
            "bonds": 0.25,
            "alternatives": 0.25,
            "cash": 0.25
        }

        # === Core Modulation Rules ===
        if emotion in ["fear", "doubt"] or urgency > 0.8:
            weights["cash"] += 0.2
            weights["equities"] -= 0.1
            weights["alternatives"] -= 0.1
        elif emotion in ["greed", "hope"]:
            weights["equities"] += 0.2
            weights["cash"] -= 0.1
            weights["bonds"] -= 0.1
        elif emotion in ["resolve", "curious"]:
            weights["alternatives"] += 0.2
            weights["cash"] -= 0.1
            weights["bonds"] -= 0.1

        # === Normalize
        total = sum(weights.values())
        for k in weights:
            weights[k] = round(weights[k] / total, 3)

        strategy = {
            "timestamp": datetime.utcnow().isoformat(),
            "weights": weights,
            "goals": goals,
            "dominant_emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "swarm_emotions": swarm_bias
        }

        self.strategy_log.append(strategy)
        return strategy

    def get_last_strategy(self):
        return self.strategy_log[-1] if self.strategy_log else {}


# === Usage Test ===
if __name__ == "__main__":
    thinker = PortfolioThinker()
    result = thinker.generate_allocation()
    print("\n[STRATEGIC PORTFOLIO]")
    print(result)