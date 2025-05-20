# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/orchestrator_portfolio_allocation_stage.py
# Purpose: Stage 4 — Portfolio Allocation and Liquidity Adjustment
# ============================================================

from finance.strategy.portfolio_thinker import PortfolioThinker
from finance.execution.emotional_liquidity_engine import EmotionalLiquidityEngine

def run_portfolio_allocation_stage(portfolio_thinker, liquidity_engine, branches, market_mood, foresight):
    report = {}

    portfolio = portfolio_thinker.allocate(branches)
    report["portfolio"] = portfolio

    adjusted_portfolio = liquidity_engine.adjust_for_mood(
        portfolio, market_mood, foresight.get("confidence", 0.6)
    )
    report["liquidity_adjusted_portfolio"] = adjusted_portfolio

    return report, adjusted_portfolio