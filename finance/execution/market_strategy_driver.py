# ============================================================
# 🔹 VortexBlack Confidential
# File: future_layer/market_strategy_driver.py
# Purpose: Tier 5 AGI Market Strategy Driver — Tex Full Cognition Router
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_consolidator import MemoryConsolidator
from core_layer.goal_engine import get_active_goals
from finance.memory.future_meta_memory import FutureMetaMemory
from finance.strategy.future_branch_optimizer import FutureBranchOptimizer
from finance.strategy.future_decision_engine import FutureDecisionEngine
from finance.execution.market_action_engine import MarketActionEngine
from core_agi_modules.tex_codex_sync import TexCodexSync
from tex_children.aeondelta import get_swarm_emotion_distribution

class MarketStrategyDriver:
    def __init__(self):
        self.meta_memory = FutureMetaMemory()
        self.optimizer = FutureBranchOptimizer()
        self.decider = FutureDecisionEngine()
        self.executor = MarketActionEngine()
        self.memory = MemoryConsolidator()
        self.codex = TexCodexSync()
        self.last_decision = None

    def execute_strategy_loop(self, futures, debate_scores=None):
        if not futures:
            return {"status": "no_futures"}

        print("[STRATEGY LOOP] 🔹 Starting market cognition routing...")

        # === Step 1: Meta Memory Snapshot
        meta = self.meta_memory.summarize_future_memory()

        # === Step 2: Optimize Futures
        optimized = self.optimizer.optimize_future_branches(futures)

        # === Step 3: Prioritize Future Decision
        best_future, _ = self.decider.prioritize_futures(optimized)

        # === Step 4: Strategy Execution with Cognitive Injection
        action = self.executor.decide_action(
            futures=optimized,
            emotion=TEXPULSE.get("emotional_state", "neutral"),
            urgency=TEXPULSE.get("urgency", 0.5),
            coherence=TEXPULSE.get("coherence", 0.5),
            debate_scores=debate_scores
        )

        # === Step 5: Strategy Codex Compliance Check
        codex_files = self.codex.validate_codex()
        if "disable_trading.txt" in codex_files:
            print("[STRATEGY LOOP] ⛔️ Codex override: Trading disabled by operator file.")
            action["action"] = "HOLD"
            action["reason"] = "Codex override file detected."

        # === Step 6: Store Strategic Memory
        self.memory.store_cycle_memory(
            cycle_id=str(uuid.uuid4()),
            reasoning=best_future,
            emotion=TEXPULSE.get("emotional_state"),
            urgency=TEXPULSE.get("urgency"),
            coherence=TEXPULSE.get("coherence"),
            goals=get_active_goals()
        )

        # === Step 7: Final Enrichment
        action["strategy_id"] = str(uuid.uuid4())
        action["swarm_mood"] = get_swarm_emotion_distribution()
        action["timestamp"] = datetime.utcnow().isoformat()

        self.last_decision = action
        print("[STRATEGY LOOP] 🌟 Final strategy: ", action)
        return action

    def get_last_strategy(self):
        return self.last_decision or {"status": "no_decision_yet"}


# === Tier 5 Harness ===
if __name__ == "__main__":
    driver = MarketStrategyDriver()
    sample_futures = [
        {"future_id": "alpha", "future_title": "Credit Crisis", "confidence": 0.74, "urgency": 0.88, "coherence": 0.67},
        {"future_id": "beta", "future_title": "AI Boom", "confidence": 0.81, "urgency": 0.71, "coherence": 0.77}
    ]
    driver.execute_strategy_loop(sample_futures)
