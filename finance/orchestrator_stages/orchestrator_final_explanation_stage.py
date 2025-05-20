# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/finance_orchestrator.py
# Purpose: Unified Financial Intelligence Loop — Tex AGI Market Foresight Brain
# ============================================================

import random
from datetime import datetime

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
from finance.strategy.alpha_paradox_engine import AlphaParadoxEngine  # ✅ Tier Ω

from finance.sentiment.market_mood_sensor import get_market_mood
from finance.triggers.phase_transition_detector import PhaseTransitionDetector
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
from core_layer.memory_engine import store_to_memory

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
        self.market_mood = None
        self.phase_detector = PhaseTransitionDetector()

        self.coherence_memory = MetaCoherenceMemory()
        self.liquidity_engine = EmotionalLiquidityEngine()
        self.alpha_voter = AlphaConsensusVoter()
        self.alpha_mimic = AlphaMimicDetector()
        self.override_reflex = CausalOverrideReflex()
        self.alpha_paradox = AlphaParadoxEngine()  # ✅ Injected Ω

    def run_cycle(self, state=None):
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

        emo_paths = self.emotions.simulate_emotional_future_paths()
        report["emotional"] = emo_paths

        causal = self.causal.generate_causal_world_graph()
        report["causal_graph"] = causal

        foresight = self.foresight.generate_forecast("hope", 0.9, 0.82)
        report["foresight"] = foresight

        tree = self.tree.generate_future_chain()
        report["tree"] = tree
        self.meta.store_future_event(random.choice(tree))

        ranked = self.decision.prioritize_futures(futures)
        branches = self.branch.optimize_future_branches(futures + emo_paths)
        report["ranked_decision"] = ranked
        report["optimized_branches"] = branches

        alpha = self.alpha.explain(ranked)
        report["alpha"] = alpha

        paradox = self.alpha_paradox.analyze_paradox(alpha, foresight, self.memory)
        report["alpha_paradox"] = paradox

        portfolio = self.thinker.allocate(branches)
        report["portfolio"] = portfolio

        portfolio = self.liquidity_engine.adjust_for_mood(
            portfolio, self.market_mood, foresight.get("confidence", 0.6))
        report["liquidity_adjusted_portfolio"] = portfolio

        regret_score = self._simulate_regret_score(portfolio, ranked)
        report["regret"] = regret_score

        if isinstance(alpha, dict) and "strategy" in alpha:
            impact_score = self.scorer.evaluate(
                strategy=alpha["strategy"],
                regret_score=regret_score,
                forecast_confidence=foresight.get("confidence", 0.6)
            )
            report["strategy_score"] = impact_score

        self.coherence_memory.log_coherence(
            regret_score=regret_score,
            foresight_confidence=foresight.get("confidence", 0.6),
            market_mood=self.market_mood
        )
        report["coherence_feedback"] = self.coherence_memory.analyze()

        store_to_memory("regret_feedback_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "score": regret_score,
            "alpha": alpha,
            "portfolio": portfolio
        })

        goal_packet = self.goal_orchestrator.generate_new_goals(
            regret_score=regret_score,
            drift_score=random.uniform(0.1, 0.6)
        )
        report["agentic_goal"] = goal_packet

        actions = self.market.decide_action(futures, "resolve", 0.9, 0.85)
        executed = self.driver.execute(actions)
        report["action"] = executed

        risk = self.risk.assess_risk(random.choice(futures))
        report["risk"] = risk

        worlds = self.multiworld.simulate_multiworld()
        insights = self.divergence.reason_over_future_worlds(worlds)
        self.multi_memory.store_multiple_worlds(worlds)
        report["multiworld_insights"] = insights

        fused_paths = self.multi_memory.recall_fused_insights()
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

        narration = self.explain_portfolio_decision(
            alpha_rationale=alpha,
            strategy=portfolio,
            foresight=foresight,
            regret_score=regret_score
        )
        report["tex_explains"] = narration

        store_to_memory("portfolio_explanations_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "explanation": narration,
            "portfolio": portfolio,
            "foresight": foresight,
            "regret_score": regret_score
        })

        print(f"\n🧐 [TEX EXPLAINS]\n{narration}")

        variants = self.variant_simulator.simulate_variants(futures, foresight.get("confidence", 0.8))
        top_variant = self.variant_simulator.rank_variants(variants)
        report["top_variant"] = top_variant

        print(f"\n🧐 [VARIANT SELECTION] Chosen strategy → {top_variant['id']} | Coherence: {top_variant['coherence']} | Regret: {top_variant['regret']}")

        phase = self.phase_detector.detect_phase_transition(regret_score, foresight.get("confidence", 0.6))
        report["phase_transition"] = phase
        store_to_memory("phase_transitions", {
            "timestamp": datetime.utcnow().isoformat(),
            "phase": phase,
            "regret": regret_score,
            "confidence": foresight.get("confidence", 0.6)
        })

        alpha_fusion = self.alpha_fuser.fuse_signals(alpha, portfolio, foresight)
        report["alpha_fusion"] = alpha_fusion
        print(f"\n🔗 [ALPHA SIGNAL FUSED] {alpha_fusion['summary']}")

        store_to_memory("alpha_signal_fusion_log", {
            "timestamp": datetime.utcnow().isoformat(),
            **alpha_fusion
        })

        vote_result = self.alpha_voter.vote(top_variant, alpha, foresight)
        report["voting_decision"] = vote_result
        print(f"\n🗳️ [ALPHA VOTE] Consensus decision: {vote_result['consensus']} ({vote_result['rationale']})")

        ghost = self.alpha_mimic.detect_ghost_strategy(alpha, futures)
        collision = self.alpha_mimic.compare_to_tex_strategy(alpha)
        report["ghost_alpha"] = ghost
        report["collision_risk"] = collision

        override = self.override_reflex.evaluate_long_term_causality(
            forecast=foresight,
            memory_trajectory=self.memory.recall_emotion_trajectory(),
            regret=regret_score,
            drift_score=random.uniform(0.5, 0.9)
        )
        if override:
            print(f"[OVERRIDE REFLEX] ⚡️ Long-horizon override triggered: {override}")
            report["override_triggered"] = override

        report["cycle_timestamp"] = datetime.utcnow().isoformat()
        return report

    def explain_portfolio_decision(self, alpha_rationale, strategy, foresight, regret_score):
        tone = foresight.get("projected_future", "uncertain")
        confidence = foresight.get("confidence", 0.0)
        reason = alpha_rationale if isinstance(alpha_rationale, str) else str(alpha_rationale)

        explanation = f"I formed my portfolio strategy under emotional tone '{tone}' "
        explanation += f"with foresight confidence {round(confidence, 2)}. "

        if regret_score > 0.6:
            explanation += f"I acknowledge regret in prior allocations (regret score: {round(regret_score, 2)}). "

        explanation += f"My allocation logic is guided by: {reason}"
        return explanation

    def _simulate_regret_score(self, portfolio, ranked):
        diversity_penalty = 1.0 if len(set(portfolio)) < 3 else 0.3
        alpha_risk_penalty = 1.0 if "uncertain" in str(ranked).lower() else 0.0
        return round((diversity_penalty + alpha_risk_penalty) / 2, 3)

if __name__ == "__main__":
    f = FinanceOrchestrator()
    full = f.run_cycle()
    for k, v in full.items():
        print(f"\n=== {k.upper()} ===\n{v}")