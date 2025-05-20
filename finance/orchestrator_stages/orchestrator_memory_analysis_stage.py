# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_memory_analysis_stage.py
# Purpose: Stage 6 — Coherence Logging, Regret Logging, and Memory Updates
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from finance.strategy.meta_coherence_memory import MetaCoherenceMemory

def run_memory_analysis_stage(coherence_memory, regret_score, foresight, market_mood, alpha, portfolio):
    report = {}

    coherence_memory.log_coherence(
        regret_score=regret_score,
        foresight_confidence=foresight.get("confidence", 0.6),
        market_mood=market_mood
    )
    report["coherence_feedback"] = coherence_memory.analyze()

    store_to_memory("regret_feedback_log", {
        "timestamp": datetime.utcnow().isoformat(),
        "score": regret_score,
        "alpha": alpha,
        "portfolio": portfolio
    })

    return report