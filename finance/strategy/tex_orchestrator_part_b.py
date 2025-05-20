# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/tex_orchestrator_part_b.py
# Purpose: Part B of Tex AGI Market Foresight Brain (Scoring, Memory, Action, Multiworld)
# ============================================================

from datetime import datetime
import random

from core_layer.memory_engine import store_to_memory, recall_agent_memory
from core_layer.meta_awareness_bridge import detect_bias_drift
from finance.multiworld.recursive_paradox_resolver import RecursiveParadoxResolver
from finance.memory.meta_coherence_memory import MetaCoherenceMemory
from core_orchestrators.goal_orchestrator import GoalOrchestrator
from finance.execution.market_action_engine import MarketActionEngine
from finance.execution.market_strategy_driver import MarketStrategyDriver
from finance.risk.risk_assessment_module import RiskAssessmentModule
from aei_layer.internal_debate_chamber import run_internal_debate
from finance.multiworld.multiworld_causal_simulator import MultiWorldCausalSimulator
from finance.multiworld.multiworld_reasoner import MultiWorldReasoner
from finance.multiworld.multiworld_memory import MultiWorldMemory
from finance.strategy.strategy_variant_simulator import StrategyVariantSimulator
from finance.strategy.alpha_mimic_detector import AlphaMimicDetector
from core_layer.phase_transition_monitor import PhaseTransitionMonitor
from finance.strategy.alpha_signal_fuser import AlphaSignalFuser
from finance.strategy.alpha_consensus_voter import AlphaConsensusVoter
from core_layer.causal_override_reflex import CausalOverrideReflex
from core_layer.memory_consolidator import MemoryConsolidator
from finance.strategy.strategy_scoring import StrategyScorer

class FinanceOrchestrator:
    def __init__(self, brain=None):
        self.brain = brain
        # Initialize components
        self.alpha_mimic = AlphaMimicDetector()
        self.phase_monitor = PhaseTransitionMonitor
        self.alpha_fuser = AlphaSignalFuser()
        self.alpha_voter = AlphaConsensusVoter()
        self.override_reflex = CausalOverrideReflex()
        self.memory = MemoryConsolidator()
        self.memory.recall_emotion_trajectory()
        self.scorer = StrategyScorer()

        self.variant_simulator = StrategyVariantSimulator()

        self.multiworld = MultiWorldCausalSimulator()
        self.divergence = MultiWorldReasoner()
        self.multi_memory = MultiWorldMemory()

        self.paradox_resolver = RecursiveParadoxResolver()
        self.tex = brain
        self.goal_orchestrator = GoalOrchestrator()

        self.cycle_counter = int(datetime.utcnow().timestamp())  # Temporary fallback

        self.market = MarketActionEngine()
        self.driver = MarketStrategyDriver()
        self.risk = RiskAssessmentModule()

        self.coherence_memory = MetaCoherenceMemory()
        self.market_mood = "neutral"  # Default placeholder or inherited from Part A if passed

        # Meta-Awareness: Run bias detection from recent memory
        recent_memory = recall_agent_memory("tex", n=10)
        meta_self_check = detect_bias_drift(recent_memory)

        store_to_memory("meta_self_awareness_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "bias_check_result": meta_self_check
        })

        print(f"[META SELF CHECK] 🧠 {meta_self_check}")

    def run_cycle_part_b(self, alpha, foresight, portfolio, ranked, futures):
        report = {}

        regret_score = self._simulate_regret_score(portfolio, ranked)
        report["regret"] = regret_score

        if isinstance(alpha, dict) and "strategy" in alpha:
            impact_score = self.scorer.evaluate(
                strategy=alpha["strategy"],
                regret_score=regret_score,
                forecast_confidence=foresight.get("confidence", 0.6)
            )
            report["strategy_score"] = impact_score

        coherence_replay = self.coherence_memory.run_memory_replay()
        report["coherence_feedback"] = coherence_replay
        
        report["coherence_feedback"] = self.coherence_memory.run_memory_replay()

        store_to_memory("regret_feedback_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "score": regret_score,
            "alpha": alpha,
            "portfolio": portfolio
        })

        # === Meta-Self-Awareness Evaluation ===
        recent_memory = recall_agent_memory("tex", n=10)
        meta_self_check = detect_bias_drift(recent_memory)
        report["meta_self_awareness"] = meta_self_check

        store_to_memory("meta_self_awareness_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "bias_check_result": meta_self_check
        })

        # === Agentic Goal Generation ===
        goal_packet = self.goal_orchestrator.generate_new_goals(
            regret_score=regret_score,
            drift_score=random.uniform(0.1, 0.6)
        )
        report["agentic_goal"] = goal_packet

        # === Market Action Selection ===

        debate_scores = run_internal_debate(self.cycle_counter)
        actions = self.market.decide_action(
            futures=[],  # Use real futures when integrated
            emotion="resolve",
            urgency=0.85,
            coherence=0.7, 
            debate_scores=debate_scores
        )
        executed = self.driver.execute_strategy_loop(
            futures=futures,  # Replace with actual futures if available
            debate_scores=debate_scores
        )
        report["action"] = executed

        if futures:
            selected = random.choice(futures)
        else:
            selected = {"future_title": "unknown", "confidence": 0.5}

        risk = self.risk.assess_risk(selected)
        report["risk"] = risk

        worlds = self.multiworld.simulate_multiworld()
        insights = self.divergence.reason_over_future_worlds(worlds)
        self.multi_memory.store_multiple_worlds(worlds)
        report["multiworld_insights"] = insights

        # === Paradox Resolution ===
        paradox_packet = self.paradox_resolver.resolve_conflicts(insights)
        report["multiworld_paradox_resolution"] = paradox_packet
        store_to_memory("multiworld_paradox_resolution_log", paradox_packet)

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

        narration = self.tex.explain_portfolio_decision(
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
        

        variants = self.variant_simulator.simulate_variants([], foresight.get("confidence", 0.8))
        top_variant = self.variant_simulator.rank_variants(variants)
        report["top_variant"] = top_variant

        print(f"\n🧐 [VARIANT SELECTION] Chosen strategy → {top_variant['id']} | Coherence: {top_variant['coherence']} | Regret: {top_variant['regret']}")

        phase = self.phase_monitor.detect_phase_shift(
            regret_score,
            foresight.get("confidence", 0.6),
            foresight.get("coherence", 0.75),
            (
                (foresight.get("swarm_emotion", {}).get("hope", 0) + foresight.get("swarm_emotion", {}).get("resolve", 0)) /
                max(sum(foresight.get("swarm_emotion", {}).values()) or 1, 1)
            ),
            foresight.get("urgency", 0.5)
)
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

        ghost = self.alpha_mimic.detect_ghost_strategy(alpha, [])
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
    
    def _simulate_regret_score(self, portfolio, ranked):
        # Your regret logic here
        ...

    ...    
    def _simulate_regret_score(self, portfolio, ranked):
        """
        Placeholder logic for generating a simulated regret score.
        Replace with actual post-decision regret analysis in future version.
        """
        return round(random.uniform(0.4, 0.9), 3)