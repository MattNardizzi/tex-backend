# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_decision_stage.py
# Purpose: Stage 2 — Decision Ranking and Future Branch Optimization
# ============================================================

from finance.strategy.future_decision_engine import FutureDecisionEngine
from finance.strategy.future_branch_optimizer import FutureBranchOptimizer

def run_decision_stage(decision_engine, branch_optimizer, futures, emo_paths):
    report = {}

    ranked = decision_engine.prioritize_futures(futures)
    optimized_branches = branch_optimizer.optimize_future_branches(futures + emo_paths)

    report["ranked_decision"] = ranked
    report["optimized_branches"] = optimized_branches

    return report, ranked, optimized_branches