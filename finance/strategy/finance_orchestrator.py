# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/finance_orchestrator.py
# Purpose: Unified Financial Intelligence Loop — Tex AGI Market Foresight Brain
# ============================================================

import random
from datetime import datetime

# === Modularized Stage Imports ===
from finance.strategy.orchestrator_input_stage import run_input_stage
from finance.strategy.orchestrator_decision_stage import run_decision_stage
from finance.strategy.orchestrator_alpha_analysis_stage import run_alpha_analysis_stage
from finance.strategy.orchestrator_portfolio_allocation_stage import run_portfolio_allocation_stage
from finance.strategy.orchestrator_strategy_scoring_stage import (
    run_strategy_scoring_stage,
    simulate_regret_score
)
from finance.strategy.orchestrator_memory_analysis_stage import run_memory_analysis_stage
from finance.strategy.orchestrator_goal_and_action_stage import run_goal_and_action_stage
from finance.strategy.orchestrator_multiworld_analysis_stage import run_multiworld_analysis_stage
from finance.strategy.orchestrator_final_explanation_stage import run_final_explanation_stage

# === Required Class Imports ===
from core_orchestrators.goal_orchestrator import GoalOrchestrator
from finance.forecasting.future_tree_generator import FutureTreeGenerator
from finance.forecasting.future_emotional_simulator import FutureEmotionalSimulator
from finance.forecasting.future_simulator import FutureSimulator
from finance.forecasting.future_causal_simulator import FutureCausalSimulator
from finance.forecasting.strategic_foresight_engine import StrategicForesightEngine
from finance.strategy.future_decision_engine import FutureDecisionEngine
from finance.strategy.portfolio_thinker import PortfolioThinker
from finance.strategy.alpha_explainer import AlphaExplainer
from finance.strategy.future_branch_optimizer import FutureBranchOptimizer
from finance.strategy.strategy_scoring import StrategyScorer
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from finance.strategy.alpha_signal_fuser import AlphaSignalFuser
from finance.strategy.meta_coherence_memory import MetaCoherenceMemory
from finance.strategy.alpha_consensus_voter import AlphaConsensusVoter
from finance.strategy.alpha_mimic_detector import AlphaMimicDetector
from finance.strategy.alpha_paradox_engine import AlphaParadoxEngine
from finance.execution.emotional_liquidity_engine import EmotionalLiquidityEngine
from finance.memory.future_memory import FutureMemory
from finance.memory.future_meta_memory import FutureMetaMemory
from finance.execution.market_action_engine import MarketActionEngine
from finance.execution.market_strategy_driver import MarketStrategyDriver
from finance.risk.risk_assessment_module import RiskAssessmentModule
from finance.multiworld.multiworld_memory import MultiWorldMemory
from finance.multiworld.multiworld_causal_simulator import MultiWorldCausalSimulator
from finance.multiworld.multiworld_reasoner import MultiWorldReasoner
from core_layer.long_horizon_override import CausalOverrideReflex

class FinanceOrchestrator:
    def __init__(self):
        self.tree = FutureTreeGenerator()
        self.emotions = FutureEmotionalSimulator()
        self.simulator = FutureSimulator()
        self.causal = FutureCausalSimulator()
        self.foresight = StrategicForesightEngine()

        self.meta = FutureMetaMemory()
        self.memory = FutureMemory()
        self.branch = FutureBranchOptimizer()
        self.alpha = AlphaExplainer()
        self.thinker = PortfolioThinker()
        self.decision = FutureDecisionEngine()
        self.scorer = StrategyScorer()
        self.variant_simulator = StrategyVariantSimulator()
        self.alpha_fuser = AlphaSignalFuser()

        self.market = MarketActionEngine()
        self.driver = MarketStrategyDriver()

        self.risk = RiskAssessmentModule()
        self.multiworld = MultiWorldCausalSimulator()
        self.divergence = MultiWorldReasoner()
        self.multi_memory = MultiWorldMemory()

        self.goal_orchestrator = GoalOrchestrator()
        self.coherence_memory = MetaCoherenceMemory()
        self.liquidity_engine = EmotionalLiquidityEngine()
        self.alpha_voter = AlphaConsensusVoter()
        self.alpha_mimic = AlphaMimicDetector()
        self.override_reflex = CausalOverrideReflex()
        self.alpha_paradox = AlphaParadoxEngine()

    def run_cycle(self):
        report = {}

        # === Stage 1: Input
        input_report, market_mood, futures, emo_paths, foresight, tree = run_input_stage(
            self.simulator, self.emotions, self.causal, self.foresight,
            self.tree, self.meta, self.memory
        )
        report.update(input_report)

        # === Stage 2: Decision
        decision_report, ranked, branches = run_decision_stage(
            self.decision, self.branch, futures, emo_paths
        )
        report.update(decision_report)

        # === Stage 3: Alpha Analysis
        alpha_report, alpha, paradox, alpha_fusion = run_alpha_analysis_stage(
            self.alpha, self.alpha_paradox, self.alpha_fuser, ranked, foresight, self.memory, None
        )
        report.update(alpha_report)

        # === Stage 4: Portfolio Allocation
        allocation_report, portfolio = run_portfolio_allocation_stage(
            self.thinker, self.liquidity_engine, branches, market_mood, foresight
        )
        report.update(allocation_report)

        # === Stage 5: Strategy Scoring
        regret_score = simulate_regret_score(portfolio, ranked)
        report["regret"] = regret_score

        score_report = run_strategy_scoring_stage(
            self.scorer, alpha, regret_score, foresight
        )
        report.update(score_report)

        # === Stage 6: Memory Analysis
        memory_report = run_memory_analysis_stage(
            self.coherence_memory, regret_score, foresight, market_mood, alpha, portfolio
        )
        report.update(memory_report)

        # === Stage 7: Goal + Action
        goal_report = run_goal_and_action_stage(
            self.goal_orchestrator, self.market, self.driver,
            self.risk, futures, regret_score, foresight
        )
        report.update(goal_report)

        # === Stage 8: Multiworld Analysis
        multiworld_report = run_multiworld_analysis_stage(
            self.multiworld, self.divergence, self.multi_memory
        )
        report.update(multiworld_report)

        # === Stage 9: Final Explanation & Voting
        final_report = run_final_explanation_stage(
            self.variant_simulator,
            self.alpha_voter,
            self.alpha_mimic,
            self.override_reflex,
            alpha,
            foresight,
            portfolio,
            futures,
            regret_score,
            self.memory
        )
        report.update(final_report)

        return report

if __name__ == "__main__":
    f = FinanceOrchestrator()
    full = f.run_cycle()
    for k, v in full.items():
        print(f"\n=== {k.upper()} ===\n{v}")