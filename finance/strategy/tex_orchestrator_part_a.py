# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/tex_orchestrator_part_a.py
# Purpose: Part A of Tex AGI Market Foresight Brain (Init + Early Forecasting)
# ============================================================

import random
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE
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
from finance.memory.meta_coherence_memory import MetaCoherenceMemory
from finance.strategy.alpha_consensus_voter import AlphaConsensusVoter
from finance.strategy.alpha_mimic_detector import AlphaMimicDetector
from finance.strategy.alpha_paradox_engine import AlphaParadoxEngine
from core_layer.causal_override_reflex import CausalOverrideReflex
from finance.sentiment.market_mood_sensor import get_market_mood
from core_layer.phase_transition_monitor import PhaseTransitionMonitor
from finance.sentiment.emotional_liquidity_engine import EmotionalLiquidityEngine

from finance.memory.future_memory import FutureMemory
from finance.memory.future_meta_memory import FutureMetaMemory

from finance.execution.market_action_engine import MarketActionEngine
from finance.execution.market_strategy_driver import MarketStrategyDriver

from finance.risk.risk_assessment_module import RiskAssessmentModule

from finance.multiworld.multiworld_memory import MultiWorldMemory
from finance.multiworld.multiworld_causal_simulator import MultiWorldCausalSimulator
from finance.multiworld.multiworld_reasoner import MultiWorldReasoner

#from core_layer.long_horizon_override import CausalOverrideReflex
from core_layer.memory_engine import store_to_memory

class FinanceOrchestrator:
    def __init__(self, brain=None):
        self.brain = brain
        # You can now access Tex via self.brain if needed
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
        self.market_mood = None
        self.phase_monitor = PhaseTransitionMonitor()

        self.coherence_memory = MetaCoherenceMemory()
        self.liquidity_engine = EmotionalLiquidityEngine()
        self.alpha_voter = AlphaConsensusVoter()
        self.alpha_mimic = AlphaMimicDetector()
        self.override_reflex = CausalOverrideReflex()
        self.alpha_paradox = AlphaParadoxEngine()

    def run_cycle_part_a(self):
        report = {}

        self.market_mood = get_market_mood()
        report["market_mood"] = self.market_mood
        store_to_memory("market_mood_adjustments", {
            "timestamp": datetime.utcnow().isoformat(),
            "mood": self.market_mood
        })

        futures = self.simulator.simulate_possible_futures()
        report["futures"] = futures
        self.memory.store_future(random.choice(futures))

        emo_paths = self.emotions.simulate_emotional_reactions()
        report["emotional"] = emo_paths

        causal = self.causal.generate_causal_world_graph()
        report["causal_graph"] = causal

        foresight = self.foresight.generate_forecast("hope", 0.9, 0.82)
        report["foresight"] = foresight

        tree = self.tree.generate_future_chain()
        report["tree"] = tree
        self.meta.store_future_event(random.choice(tree))

        ranked_titles = self.decision.prioritize_futures(futures)
        branches = self.branch.optimize_future_branches(futures + emo_paths)
        report["ranked_decision"] = ranked_titles
        report["optimized_branches"] = branches

        # ✅ Filter the original futures to get full dicts matching the ranked titles
        ranked = [f for f in futures if f.get("future") in ranked_titles or f.get("future_title") in ranked_titles]

        alpha = self.alpha.explain_alpha_origin(ranked)
        report["alpha"] = alpha

        paradox = self.alpha_paradox.analyze_contradiction(alpha, foresight, self.memory)
        report["alpha_paradox"] = paradox

        portfolio = self.thinker.generate_allocation()
        report["portfolio"] = portfolio

        portfolio = self.liquidity_engine.adjust_portfolio(
            TEXPULSE.get("emotional_state", "neutral"),
            TEXPULSE.get("urgency", 0.6),
            TEXPULSE.get("coherence", 0.7),
            portfolio
        )
        report["liquidity_adjusted_portfolio"] = portfolio

        return report, alpha, foresight, portfolio, ranked, futures
