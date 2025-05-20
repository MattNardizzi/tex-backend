# ============================================================
# 🔹 VortexBlack Confidential
# File: market_action_engine.py
# Purpose: TIER 6 AGI Market Execution Core — Tex Cognitive Fusion Layer
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import math
from datetime import datetime

from finance.memory.future_meta_memory import FutureMetaMemory
from dream_layer.dream_fusion_engine import DreamFusionEngine
from core_layer.memory_consolidator import MemoryConsolidator
from tex_children.aeondelta import get_swarm_emotion_distribution
from core_layer.goal_engine import get_active_goals
from core_layer.goal_inference_engine import GoalInferenceEngine
from core_agi_modules.tex_codex_sync import TexCodexSync

class MarketActionEngine:
    def __init__(self):
        self.last_actions = []
        self.memory = MemoryConsolidator()
        self.meta_memory = FutureMetaMemory()
        self.dream_engine = DreamFusionEngine()
        self.swarm_emotions = get_swarm_emotion_distribution
        self.goal_trace = GoalInferenceEngine()
        self.codex = TexCodexSync()

        self.behavioral_bias_map = {
            "fear": "DEFENSIVE",
            "doubt": "DEFENSIVE",
            "greed": "AGGRESSIVE",
            "hope": "AGGRESSIVE",
            "resolve": "STRATEGIC",
            "curious": "STRATEGIC",
            "anger": "RECKLESS",
            "joy": "EXPANSIVE"
        }

    def decide_action(self, futures, emotion, urgency, coherence, debate_scores=None, override_bias=None):
        if not futures:
            return {"action": "HOLD", "confidence": 0.3, "reason": "No futures supplied."}

        top = sorted(futures, key=lambda x: x.get("confidence", 0), reverse=True)[0]
        bias = override_bias or self.behavioral_bias_map.get(emotion, "NEUTRAL")
        volatility = 1.0 - coherence
        decision = "HOLD"

        # === Dream Conflict Check ===
        dream_projection = self.dream_engine.generate_dream_projection()
        if dream_projection and top["future_title"] in str(dream_projection):
            volatility += 0.1

        # === Memory Recall Trace ===
        mem_snap = self.memory.get_recent_memory(limit=1)
        last_goal = get_active_goals()[0] if get_active_goals() else "none"
        reason_entry = self.goal_trace.infer_reason(last_goal, emotion, urgency, top["confidence"])

        # === Core Logic Matrix ===
        if bias == "DEFENSIVE":
            decision = "LIQUIDATE" if urgency > 0.85 else "HEDGE"
        elif bias == "AGGRESSIVE":
            decision = "BUY_HEAVY" if top["confidence"] > 0.8 else "BUY_SELECTIVE"
        elif bias == "STRATEGIC":
            decision = "REBALANCE" if urgency > 0.75 and coherence > 0.75 else "DIVERSIFY"
        elif bias == "RECKLESS":
            decision = "LEVERAGE_PUSH" if random.random() > 0.5 else "SWING_TRADE"
        elif bias == "EXPANSIVE":
            decision = "SECTOR_ROTATE" if top["confidence"] > 0.65 else "SCAN_EMERGING"

        # === Internal Debate Override ===
        if debate_scores:
            winning_agent = max(debate_scores, key=lambda x: x["score"])
            if winning_agent["score"] < 0.6:
                decision = "WAIT_SIGNAL"

        # === Mutation Edge ===
        if urgency > 0.92 and coherence < 0.6 and random.random() < 0.25:
            decision = "MUTATION_TRADE"

        # === Codex Sync Check ===
        codex_files = self.codex.validate_codex()
        if codex_files and "restricted_sectors.txt" in codex_files:
            if "energy" in top["future_title"].lower():
                decision = "AVOID_SECTOR"

        action_plan = {
            "action": decision,
            "bias": bias,
            "future": top.get("future_title", "unknown"),
            "confidence": round(top.get("confidence", 0), 3),
            "volatility": round(volatility, 3),
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "swarm_emotion": self.swarm_emotions(),
            "goal_trace": reason_entry,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.last_actions.append(action_plan)
        return action_plan

    def get_recent_actions(self, limit=5):
        return self.last_actions[-limit:]

# === AGI Test Harness ===
if __name__ == "__main__":
    engine = MarketActionEngine()
    futures = [
        {"future_title": "Global Supply Chain Crisis", "confidence": 0.87},
        {"future_title": "Crypto Winter Thaw", "confidence": 0.65}
    ]
    scores = [
        {"agent": "debate_0", "score": 0.55},
        {"agent": "debate_1", "score": 0.77},
        {"agent": "debate_2", "score": 0.84}
    ]
    print(engine.decide_action(futures, emotion="greed", urgency=0.94, coherence=0.51, debate_scores=scores))