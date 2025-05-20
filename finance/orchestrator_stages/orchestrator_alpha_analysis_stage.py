# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_alpha_analysis_stage.py
# Purpose: Stage 3 — Alpha Explanation, Paradox Detection, and Signal Fusion
# ============================================================

from finance.strategy.alpha_explainer import AlphaExplainer
from finance.strategy.alpha_paradox_engine import AlphaParadoxEngine
from finance.strategy.alpha_signal_fuser import AlphaSignalFuser

def run_alpha_analysis_stage(alpha_explainer, alpha_paradox, alpha_fuser, ranked, foresight, memory, portfolio):
    report = {}

    alpha = alpha_explainer.explain(ranked)
    report["alpha"] = alpha

    paradox = alpha_paradox.analyze_paradox(alpha, foresight, memory)
    report["alpha_paradox"] = paradox

    alpha_fusion = alpha_fuser.fuse_signals(alpha, portfolio, foresight)
    report["alpha_fusion"] = alpha_fusion

    return report, alpha, paradox, alpha_fusion