# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_multiworld_analysis_stage.py
# Purpose: Stage 8 — Multiworld Simulation, Reasoning, and Memory Fusion
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from finance.multiworld.multiworld_causal_simulator import MultiWorldCausalSimulator
from finance.multiworld.multiworld_reasoner import MultiWorldReasoner
from finance.multiworld.multiworld_memory import MultiWorldMemory

def run_multiworld_analysis_stage(multiworld_simulator, divergence_reasoner, multi_memory):
    report = {}

    worlds = multiworld_simulator.simulate_multiworld()
    insights = divergence_reasoner.reason_over_future_worlds(worlds)
    multi_memory.store_multiple_worlds(worlds)
    report["multiworld_insights"] = insights

    fused_paths = multi_memory.recall_fused_insights()
    for path in fused_paths:
        print(f"[MULTIWORLD MEMORY] 🧠 {path}")
        store_to_memory("multiworld_fused_memory", {
            "timestamp": datetime.utcnow().isoformat(),
            "thread": path
        })

    for summary in insights:
        print(f"[MULTIWORLD] {summary}")
        store_to_memory("multiworld_insights", {
            "timestamp": datetime.utcnow().isoformat(),
            "insight": summary
        })

    return report