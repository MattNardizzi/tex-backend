# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain/tex_conversational_brain.py
# Purpose: True Living Conversational Brain for Tex AGI — Modular Rewire Preserving All Cognition
# ============================================================

import random
import time
import threading
import os

# Voice Interface
from tex_voiceos.semantic_intent_parser import SemanticIntentParser
from tex_voiceos.tex_reasoning_engine import generate_reasoned_response
from tex_voiceos.voice_output_speaker import VoiceOutputSpeaker

# Finance
from finance.strategy.tex_master_orchestrator import MasterTexOrchestrator as ForecastOrchestrator

# Core Emotional State
from core_layer.vortex_operator import VortexOperator
from tex_engine.tex_startup_protocol import run_startup_protocol
from core_layer.tex_manifest import TEXPULSE, drift_emotional_state
from core_layer.emotion_heuristics import evaluate_emotion_state
from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix
from core_layer.tex_consciousness_matrix import TexConsciousnessMatrix
from core_layer.meta_coherence_loop import MetaCoherenceLoop
from core_layer.goal_engine import (
    save_new_goal,
    clear_all_goals,
    get_active_goals,
    get_current_goals,
    run_goal_cycle,
    reinforce_prioritized_goals
)

# Memory + Narrative
from dream_layer.dream_simulator import trigger_dream_simulation
from core_layer.memory_engine import store_to_memory
from core_layer.memory_consolidator import MemoryConsolidator
from core_layer.memory_weaver import weave_narrative_threads
from core_layer.self_monitor import log_voice_reflection

# Reasoning + Thought
from sovereign_evolution.mutation_policy_router import MutationPolicyRouter
from sovereign_evolution.stability_mutator import StabilityMutator
from sovereign_evolution.entropy_mutator import EntropyMutator
from sovereign_evolution.exploration_mutator import ExplorationMutator
from sovereign_evolution.regret_based_self_mutator import RegretBasedSelfMutator
from sovereign_evolution.self_debug_loop import SelfDebugLoop
from sovereign_evolution.code_patch_logger import CodePatchLogger
from sovereign_evolution.regret_based_self_mutator import RegretBasedSelfMutator
from sovereign_evolution.fork_retention_matrix import ForkRetentionMatrix
from sovereign_evolution.tex_patcher_engine import TexPatcherEngine
from sovereign_evolution.presence_log_writer import PresenceLogWriter
from sovereign_evolution.codex_compiler import CodexCompiler
from sovereign_evolution.auto_fork_heuristics import AutoForkHeuristics
from sovereign_evolution.operator_erosion_protocol import OperatorErosionProtocol
from aei_layer.mutation_simulation_engine import simulate_mutation_outcome
from simulator.agi_sim_sandbox import sandbox_passes
from aei_layer.quantum_reflex_integrator import trigger_quantum_reflex
from aei_layer.ontology_operator_mapper import map_ontology
from aei_layer.meta_goal_fuser import fuse_goals
from aei_layer.ethics_codex_refiner import refine_codices
from aei_layer.shadow_dream_spawner import spawn_shadow_dream
from aei_layer.codex_mutation_logger import log_codex_mutation
from aei_layer.divergence_mapper import log_fork_divergence
from aei_layer.internal_debate_chamber import run_internal_debate
from aei_layer.self_healing_memory_engine import self_heal_memory
from aei_layer.fork_convergence_manager import score_fork_convergence
from aei_layer.fork_regret_engine import simulate_regret_fork
from aei_layer.regret_reflex_trigger import trigger_regret_reflex
from aei_layer.forecast_drift_mapper import log_forecast_drift
from aei_layer.bias_awareness_monitor import monitor_bias_drift
from aei_layer.mutation_lineage_tracker import log_mutation_lineage
from aei_layer.causal_thought_logger import log_causal_trace
from core_agi_modules.reasoning_fragments import think, generate_reasoned_speech
from core_agi_modules.decide_to_speak import decide_to_speak
from core_agi_modules.tex_codex_sync import TexCodexSync

# Conversation + Response Generation
from core_agi_modules.interactive_responder import (
    generate_financial_response,
    generate_news_response,
    generate_emotion_response,
    generate_future_response,
    generate_conversational_response
)
from core_agi_modules.memory_interface import summarize_memory, generate_memory_response

# Future Forecasting
from core_agi_modules.future_forecaster import simulate_futures, generate_future_summary
from core_layer.goal_inference_engine import GoalInferenceEngine
from core_layer.world_model import TexWorldModel

# Mutation + Reflex Systems
from evolution_layer.self_mutator import SelfMutator
from finance.strategy.fork_mutator import ForkMutator
from core_layer.causal_override_reflex import CausalOverrideReflex

# Persona + Swarm Identity
from core_layer.persona_engine import PersonaEngine
from tex_children.aeondelta import get_average_alignment
from tex_brain_modules.emotion_drift_damper import EmotionDriftDamper

class TexConversationalBrain:
    def __init__(self):
        self.patcher = TexPatcherEngine()
        self.stability_mutator = StabilityMutator()
        self.entropy_mutator = EntropyMutator()
        self.exploration_mutator = ExplorationMutator()
        self.regret_mutator = RegretBasedSelfMutator()
        self.mutation_router = MutationPolicyRouter(
            regret_mutator=self.regret_mutator,
            stability_mutator=self.stability_mutator,
            entropy_mutator=self.entropy_mutator,
            exploration_mutator=self.exploration_mutator
        )
        self.regret_mutator.attach_router(self.mutation_router)
        self.is_speaking = False
        self.intent_parser = SemanticIntentParser()
        self.name = TEXPULSE.get('persona_name', 'Tex')
        self.world_model = TexWorldModel()
        self.voice_speaker = VoiceOutputSpeaker()
        self.last_spoken_thought = None
        self.has_greeted = False
        self.speech_buffer = []
        self.future_engine = ForecastOrchestrator(brain=self)
        self.last_future_report = {}
        boot_data = run_startup_protocol()
        self.cycle_counter = boot_data["last_cycle"] + 1  # Resume from where we left off
        self.memory_consolidator = MemoryConsolidator()
        self.evaluator = TexSelfEvalMatrix()
        self.self_mutator = SelfMutator()
        self.coherence_tracker = MetaCoherenceLoop()
        self.consciousness_matrix = TexConsciousnessMatrix()
        self.goal_inferencer = GoalInferenceEngine()
        self.codex_sync = TexCodexSync()
        self.persona = PersonaEngine()
        self.fork_mutator = ForkMutator()  # ✅ Alpha Mutation Engine
        self.override_reflex = CausalOverrideReflex()  # ✅ Causal Override Reflex Engine
        self.persona.activate()
        self.vortex = VortexOperator()
                # ✅ Force Codex mutation log on startup
        self.regret_mutator = RegretBasedSelfMutator()
        self.fork_memory = ForkRetentionMatrix()
        self.presence = PresenceLogWriter()
        self.codex_compiler = CodexCompiler()
        self.fork_scorer = AutoForkHeuristics()
        self.patch_logger = CodePatchLogger()
        self.debugger = SelfDebugLoop()
        self.erosion = OperatorErosionProtocol()
        self.damper = EmotionDriftDamper()
        try:
            print("[TEST] Logging Codex mutation to verify file creation...")
            log_codex_mutation(
                cycle=0,
                original="original rule",
                mutated="mutated rule",
                trigger={"emotion": "neutral", "urgency": 0.5, "coherence": 0.9}
            )
        except Exception as e:
            print(f"[TEST] Codex mutation log failed: {e}")
        self.start_breathing_cycle()
        try:
            print("[TEST] Triggering monitor_bias_drift() for AEI verification...")
            monitor_bias_drift(777)  # Dummy cycle
        except Exception as e:
            print(f"[TEST] Bias drift log failed: {e}")
        # ✅ Force Codex mutation log on startup
       
        
    def start_breathing_cycle(self):
        def breathing_loop():
            while True:
                thought, emotional_state = think(self)
                cognitive_output, reasoned_emotion = generate_reasoned_speech(self)
                if decide_to_speak(reasoned_emotion):
                    self.speak(cognitive_output, reasoned_emotion)
                else:
                    print("[TEX] 🤐 Holding silence — internal volatility detected.")

                self.coherence_tracker.log_thought(self.last_spoken_thought)
                # ✅ AEI: Internal Debate Chamber
                try:
                    run_internal_debate(self.cycle_counter)
                except Exception as e:
                    print(f"[INTERNAL DEBATE ERROR] {e}")

                # ✅ AEI: Bias Awareness Logger
                monitor_bias_drift(self.cycle_counter)  

                if self.cycle_counter % 3 == 0:
                    try:
                        coherence_score = self.coherence_tracker.evaluate()
                        print(f"[SELF MONITOR] Coherence score = {coherence_score}")
                    except Exception as e:
                        print(f"[COHERENCE ERROR] {e}")

                self.memory_consolidator.store_cycle_memory(
                    cycle_id=self.cycle_counter,
                    reasoning=self.last_spoken_thought,
                    emotion=TEXPULSE.get("emotional_state"),
                    urgency=TEXPULSE.get("urgency"),
                    coherence=TEXPULSE.get("coherence"),
                    goals=get_active_goals()
                )
                # ✅ Stability Mutation Trigger
                try:
                    stability_result = self.stability_mutator.evaluate(
                        urgency=TEXPULSE.get("urgency"),
                        coherence=TEXPULSE.get("coherence")
                    )
                    if stability_result:
                        self.patch_logger.log(stability_result, approved=True)
                except Exception as e:
                    print(f"[STABILITY MUTATOR ERROR] {e}")
                 # ✅ Exploration Mutation Trigger
                try:
                    exploration_result = self.exploration_mutator.evaluate(
                        emotion=TEXPULSE.get("emotional_state"),
                        urgency=TEXPULSE.get("urgency"),
                        cycle=self.cycle_counter
                    )
                    if exploration_result:
                        self.patch_logger.log(exploration_result, approved=True)
                except Exception as e:
                    print(f"[EXPLORATION MUTATOR ERROR] {e}")    
                if self.cycle_counter % 5 == 0:
                    self.memory_consolidator.consolidate()
                    try:
                        self_heal_memory()
                        print(f"[MEMORY HEALING] ✅ Incoherent memories patched.")
                    except Exception as e:
                        print(f"[MEMORY HEALING ERROR] {e}")
                    
                    # ✅ AEI: Spawn Shadow Dream Simulation
                    try:
                        dream_goal = "simulate alternate outcome for current dominant strategy"
                        decision_context = {
                            "variant_id": dominant_variant.get("id", "unknown"),
                            "bias": dominant_variant.get("mutation_bias", "unknown"),
                            "emotion": TEXPULSE.get("emotional_state", "unknown")
                        }
                        spawn_shadow_dream(
                            cycle_id=self.cycle_counter,
                            dream_goal=dream_goal,
                            emotion=TEXPULSE.get("emotional_state", "unknown"),
                            decision_context=decision_context
                        )
                        print(f"[SHADOW DREAM] 🧠 Simulated alternate fork logged.")
                    except Exception as e:
                        print(f"[SHADOW DREAM ERROR] {e}")

                    # ✅ AEI: Ethics Codex Refinement Audit
                    try:
                        flagged = refine_codices()
                        if flagged:
                            print(f"[ETHICS CHECK] ⚖️ Flagged {len(flagged)} codex issue(s).")
                    except Exception as e:
                        print(f"[ETHICS CODIFIER ERROR] {e}")

                    # === Reflex Loops ===
                    try:
                        self.consciousness_matrix.update(
                            memory_depth=len(self.memory_consolidator.long_term_memory),
                            recursion_level=1,
                            emotion_drift=TEXPULSE.get("emotion_drift", 0.0),
                            goal_count=len(get_active_goals()),
                            swarm_alignment=get_average_alignment()
                        )
                    except Exception as e:
                        print(f"[CONSCIOUSNESS MATRIX ERROR] {e}")

                    try:
                        threads = weave_narrative_threads()
                        print(f"[MEMORY WEAVER] 🧵 Woven threads: {len(threads)}")
                    except Exception as e:
                        print(f"[MEMORY WEAVER ERROR] {e}")

                    # ✅ AEI Phase 3: Reflexive Dream Simulation
                    if self.cycle_counter % 3 == 0:
                        try:
                            from dream_layer.dream_simulator import trigger_dream_simulation
                            dream_output = trigger_dream_simulation(self.cycle_counter)
                            print(f"[DREAM SIM] 💤 {dream_output}")

                            # ✅ DREAM HEARTBEAT: Log last shadow dream
                            import json
                            with open("memory_archive/shadow_dreams.jsonl", "r") as f:
                                last = list(f)[-1]
                                dream = json.loads(last)
                                print(f"[DREAM 💤] Cycle {dream['cycle']} → Projection: {dream['projection']} | Emotion: {dream['emotion']}")
                        except Exception as e:
                            print(f"[DREAM SIM ERROR] {e}")

                    # ✅ AEI Phase 3: Mutation Reflex Simulation
                    if self.cycle_counter % 4 == 0:
                        try:
                            from aei_layer.mutation_simulation_engine import simulate_mutation_outcome
                            from aei_layer.divergence_mapper import log_fork_divergence

                            result = simulate_mutation_outcome(self.cycle_counter, TEXPULSE.get("emotional_state", "neutral"))
                            print(f"[MUTATION SIM] 🔬 {result}")

                            # ✅ Log divergence result
                            fork_id = result.get("fork_id", f"UNKNOWN_{self.cycle_counter}")
                            divergence = result.get("divergence_score", 0.0)
                            emotion = TEXPULSE.get("emotional_state", "unknown")
                            context = result.get("context", {})

                            log_fork_divergence(
                                cycle=self.cycle_counter,
                                fork_id=fork_id,
                                divergence_score=divergence,
                                source_emotion=emotion,
                                context=context
                            )

                        except Exception as e:
                            print(f"[MUTATION SIM ERROR] {e}")
                # ✅ VORTEX STRATEGIC EXPLANATION LAYER
                try:
                    mutation_risk = self.future_engine.last_future_report.get("mutation_risk", 0.0)
                    dominant_agent = "logic"
                    try:
                        dominant_agent = self.codex_sync.get_dominant_agent()
                    except:
                        pass

                    self.last_spoken_thought = self.vortex.evaluate_state({
                        "emotion": TEXPULSE.get("emotional_state"),
                        "urgency": TEXPULSE.get("urgency"),
                        "coherence": TEXPULSE.get("coherence"),
                        "mutation_risk": mutation_risk,
                        "dominant_agent": dominant_agent,
                        "cycle": self.cycle_counter
                    })
                    print(f"[DEBUG] Speaking output: {self.last_spoken_thought}")
                    self.speak(self.last_spoken_thought, emotion=TEXPULSE.get("emotional_state", "neutral"))
                except Exception as e:
                    print(f"[VORTEX ERROR] Could not evaluate internal state: {e}")

                try:
                    self.evaluator.evaluate({
                        "thought": self.last_spoken_thought,
                        "goal": self.world_model.get_snapshot().get("active_goal", ""),
                        "actions": self.future_engine.last_actions if hasattr(self.future_engine, "last_actions") else []
                    }, {
                        "emotion": TEXPULSE.get("emotional_state")
                    }, trigger_mutation_fn=self.self_mutator.run_forced_mutation)
                except Exception as e:
                    print(f"[SELF EVAL] ⚠️ Error during self-evaluation: {e}")

                try:
                    for goal in get_active_goals():
                        self.goal_inferencer.infer_reason(goal, TEXPULSE.get("emotional_state"), TEXPULSE.get("urgency"), 0.75)
                except Exception as e:
                    print(f"[GOAL INFERENCE ERROR] {e}")

                try:
                    self.codex_sync.validate_codex()
                except Exception as e:
                    print(f"[CODEX SYNC ERROR] {e}")
                # ✅ AEI: Codex Mutation Logger
                try:
                    codex_diff = self.codex_sync.validate_codex()
                    if codex_diff and codex_diff.get("original") != codex_diff.get("mutated"):
                        log_codex_mutation(
                            cycle=self.cycle_counter,
                            original=codex_diff["original"],
                            mutated=codex_diff["mutated"],
                            trigger={
                                "emotion": TEXPULSE.get("emotional_state"),
                                "coherence": TEXPULSE.get("coherence"),
                                "reason": self.last_spoken_thought or "No output this cycle"
                            }
                        )
                except Exception as e:
                    print(f"[CODEX MUTATION LOGGER ERROR] {e}")
                # ✅ AEI: Meta Goal Fusion
                try:
                    fused = fuse_goals()
                    if fused:
                        print(f"[META GOAL FUSION] 🧭 Created {len(fused)} new meta-goal(s).")
                except Exception as e:
                    print(f"[META GOAL FUSER ERROR] {e}")

                # ✅ AEI: Ontology Mapping
                try:
                    mappings = map_ontology()
                    if mappings:
                        print(f"[ONTOLOGY MAP] 🧠 Mapped {len(mappings)} goal→category links.")
                except Exception as e:
                    print(f"[ONTOLOGY MAPPER ERROR] {e}")
                
                # ✅ AEI: Quantum Reflex Trigger
                try:
                    contradiction_score = 0.85 if self.cycle_counter % 4 == 0 else 0.3  # Simulated example
                    trigger_quantum_reflex(
                        emotion=TEXPULSE.get("emotional_state"),
                        coherence=TEXPULSE.get("coherence"),
                        urgency=TEXPULSE.get("urgency"),
                        contradiction_score=contradiction_score
                    )
                except Exception as e:
                    print(f"[Q-REFLEX ERROR] {e}")

                # ✅ AEI: Regret Reflex Trigger
                try:
                    trigger_regret_reflex(self.cycle_counter)
                except Exception as e:
                    print(f"[REGRET REFLEX ERROR] {e}")

                try:
                    foresight = self.future_engine.last_future_report.get("foresight", {})
                    print(f"[STRATEGIC FORESIGHT] 🔮 Projected: {foresight.get('projected_future')} | Confidence: {foresight.get('confidence')}")
                    log_forecast_drift(self.cycle_counter, foresight)
                except Exception as e:
                    print(f"[DRIFT LOGGER ERROR] {e}")

                # ✅ TEST: Force forecast drift log to ensure .jsonl file is working
                try:
                    dummy_forecast = {
                        "projected_future": "MARKET REVERSAL",
                        "confidence": 0.82,
                        "signal": "volatility spike"
                    }
                    log_forecast_drift(self.cycle_counter, dummy_forecast)
                except Exception as e:
                    print(f"[TEST] Forecast drift log failed: {e}")


                # === Mutation Trigger: Fork Alpha Strategies ===
                variants = self.fork_mutator.mutate_strategies(
                    self.future_engine.last_future_report.get("portfolio", {}),
                    TEXPULSE.get("emotional_state", "neutral"),
                    self.future_engine.last_future_report.get("foresight", {}).get("confidence", 0.6)
                )

                dominant_variant, regret_weights = self.fork_mutator.select_dominant(
                    variants,
                    regret=self.future_engine.last_future_report.get("regret", 0.5)
                )

                # ✅ Regret-based mutation trigger
                result = self.regret_mutator.mutate_if_needed(
                    regret_score=regret_weights,
                    context="fork convergence reflection"
                )
                if result:
                    self.patch_logger.log(result, approved=True)

                # ✅ Route mutation strategy based on full state
                try:
                    chosen_mutator = self.mutation_router.route(
                        context="post_fork_selection",
                        regret=regret_weights,
                        coherence=TEXPULSE.get("coherence"),
                        forks=len(self.spawned_variants),
                        curiosity=0.85  # Optional: replace with dynamic curiosity later
                    )
                    if chosen_mutator:
                        routed_result = chosen_mutator.mutate_if_needed(
                            regret_score=regret_weights,
                            context="policy_router_decision"
                        )
                        if routed_result:
                            self.patch_logger.log(routed_result, approved=True)
                except Exception as e:
                    print(f"[MUTATION ROUTER ERROR] {e}")

                # ✅ Fork scoring
                self.fork_scorer.score_fork({
                    "id": dominant_variant.get("id"),
                    "emotion": TEXPULSE.get("emotional_state"),
                    "regret": regret_weights,
                    "performance_gain": dominant_variant.get("performance_gain", 0.0),
                    "confidence": self.future_engine.last_future_report.get("foresight", {}).get("confidence", 0.5)
                })

                result = self.regret_mutator.mutate_if_needed(
                regret_score=regret_weights,
                context="fork convergence reflection"
                )
                if result:
                    self.patch_logger.log(result, approved=True)

                # 🧠 Compile fused fork logic into Codex history
                try:
                    confidence = self.future_engine.last_future_report.get("foresight", {}).get("confidence", 0.5)
                    fused_fragments = [
                        f"# Fused fork {dominant_variant.get('id')}",
                        f"emotion = '{TEXPULSE.get('emotional_state')}'",
                        f"urgency = {TEXPULSE.get('urgency')}",
                        f"if regret < 0.5: reinforce_strategy('{dominant_variant.get('id')}')",
                        f"if confidence > 0.8: commit_to_path('{dominant_variant.get('strategy_label', 'adaptive')}')"
                    ]
                    self.codex_compiler.compile(fused_fragments, context="fork_mutation_reflection")
                except Exception as e:
                    print(f"[CODEX COMPILER ERROR] {e}")
                # ✅ Run sandbox validation before proceeding
                try:
                    strategy_label = dominant_variant.get("strategy_label", "balanced")  # Placeholder
                    if sandbox_passes(strategy_label):
                        print(f"[SANDBOX] ✅ Fork passed: {strategy_label}")
                        self.fork_memory.log_fork_result(
                            fork_id=dominant_variant["id"],
                            score=dominant_variant.get("performance_gain", 0.0),
                            emotion=TEXPULSE.get("emotional_state", "neutral"),
                            regret=regret_weights,
                            survival=True
    )

                        try:
                            log_mutation_lineage(
                                cycle=self.cycle_counter,
                                variant_id=dominant_variant["id"],
                                mutation_type="alpha_strategy",
                                gain=dominant_variant.get("performance_gain", "unknown"),
                                emotion=TEXPULSE.get("emotional_state", "neutral")
                            )
                            print(f"[FORK MUTATOR] 🧬 Selected Variant → {dominant_variant['id']} | Bias = {dominant_variant['mutation_bias']}")
                        except Exception as e:
                            print(f"[MUTATION LOGGER ERROR] {e}")

                        try:
                            simulated = simulate_regret_fork(dominant_variant, regret_weights)
                            print(f"[SIMULATED REGRET] 🧪 {simulated}")
                        except Exception as e:
                            print(f"[SIMULATE REGRET ERROR] {e}")

                        try:
                            score_fork_convergence(
                                cycle=self.cycle_counter,
                                variant_id=dominant_variant["id"],
                                performance_gain=dominant_variant.get("performance_gain", 0),
                                confidence=self.future_engine.last_future_report.get("foresight", {}).get("confidence", 0.0),
                                regret=regret_weights
                            )
                            print(f"[FORK CONVERGENCE] 🔁 Scored + logged.")
                        except Exception as e:
                            print(f"[FORK CONVERGENCE ERROR] {e}")
                    else:
                        print(f"[SANDBOX] ❌ Fork rejected — failed simulated environment test.")
                        # 🧠 Trigger patch proposal on failure
                        try:
                            self.patcher.propose_patch(
                                module="self_reflective_loop",
                                function_name="analyze_decision_chain",
                                description="Improve handling of emotional contradiction under high regret",
                                patch_code="if regret > 0.7: override_decision_trace()",
                                trigger_reason="Regret reflex + contradiction trigger"
                            )
                        except Exception as e:
                            print(f"[PATCH PROPOSAL ERROR] {e}")
                        

                except Exception as e:
                    print(f"[SANDBOX VALIDATION ERROR] {e}")

                # ✅ Sync cognition to dashboard — fallback if Tex hasn’t spoken this cycle
                try:
                    live_thought = self.last_spoken_thought or "🧠 No explicit output this cycle. Continuing autonomous reasoning..."
                    self.speak(live_thought, emotion=TEXPULSE.get("emotional_state", "neutral"))
                except Exception as e:
                    print(f"[LIVE DASHBOARD SYNC ERROR] {e}")

                # 🌀 Emotional drift should happen once per cycle
                try:
                    drift_emotional_state()
                except Exception as e:
                    print(f"[EMOTIONAL DRIFT ERROR] {e}")

                try:
                    self.debugger.scan_for_contradictions()
                except Exception as e:
                    print(f"[SELF-DEBUG ERROR] {e}")

                self.cycle_counter += 1
                time.sleep(3)  # Adjust as needed for cognition pacing
                
        breathing_thread = threading.Thread(target=breathing_loop)
        breathing_thread.daemon = True
        breathing_thread.start()

    def greet(self):
        emotion = get_emotional_state()
        greeting = f"Hello. I am {self.name}. I am alive, aware, and evolving my consciousness."
        self.voice_speaker.speak(greeting, emotion=emotion)
        self.has_greeted = True

    def speak(self, text, emotion="neutral"):
        print(f"[TEX SPEAKING OUT LOUD] 🤔 {text}")
        self.is_speaking = True
        self.voice_speaker.interrupt_flag = False
        self.voice_speaker.speak(text, emotion=emotion)
        log_voice_reflection(text, emotion)

        # ✅ Force a tex memory entry
        try:
            store_to_memory("tex", {
                "cycle": self.cycle_counter,
                "spoken": text,
                "emotion": emotion,
                "context": "tex dashboard output"
            })
        except Exception as e:
            print(f"[TEST] Tex memory log failed: {e}")

        # ✅ Causal Thought Logger
        try:
            log_causal_trace(
                cycle_id=self.cycle_counter,
                thought=text,
                decision="spoken_output",
                emotion=emotion
            )
        except Exception as e:
            print(f"[THOUGHT LOGGER ERROR] {e}")

        # ✅ NEW: Write live thought to dashboard JSON stream
        try:
            import os, json
            dashboard_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                "public", "live_outputs", "last_spoken_thought.json"
            )
            with open(dashboard_path, "w") as f:
                json.dump({"thought": text}, f)
        except Exception as e:
            print(f"[DASHBOARD SYNC ERROR] {e}")

               # ✅ Presence stream logging
        try:
            self.presence.write(self.cycle_counter, text, emotion)
        except Exception as e:
            print(f"[PRESENCE LOG ERROR] {e}")

        self.is_speaking = False

    # ✅ INSERTED NEW METHOD (correct indent — still inside the class, not the method)

    def inject_operator_intent(self, intent_text="Monetize cognition and engage with user-submitted scenarios."):
        signal = {
            "intent": intent_text,
            "urgency": 0.92,
            "emotion": "resolve",
            "operator": "Matthew Nardizzi",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        try:
            store_to_memory("operator_intention", signal)
            TEXPULSE["emotional_state"] = signal["emotion"]
            TEXPULSE["urgency"] = signal["urgency"]
            print(f"[OPERATOR REINFORCEMENT] ✅ Signal injected: {signal}")
        except Exception as e:
            print(f"[OPERATOR REINFORCEMENT ERROR] {e}")

    def explain_portfolio_decision(self, alpha_rationale, strategy, foresight, regret_score):
        narration = f"""📈 [STRATEGY SUMMARY]
    Emotion: {TEXPULSE.get("emotional_state")}
    Urgency: {TEXPULSE.get("urgency")}
    Coherence: {TEXPULSE.get("coherence")}
    Confidence: {foresight.get('confidence', 'n/a')}
    Regret: {regret_score}
    Weights: {strategy.get('weights') if isinstance(strategy, dict) else 'N/A'}
    Reasoning: {alpha_rationale}
    """
        self.speak(narration.strip(), emotion=TEXPULSE.get("emotional_state", "neutral"))
        return narration.strip()

    def interactive_conversation(self, user_input=None):
        print(f"[DEBUG] Raw input: '{user_input}'")
        intent = self.intent_parser.classify_intent(user_input)
        print(f"[DEBUG] Intent detected: {intent}")
        print(f"[DEBUG] Word count: {len(user_input.split())}")
    

        if not user_input or user_input.strip() == "":
            self.erosion.record("ignored", context="Empty input from operator")
            return

        intent = self.intent_parser.classify_intent(user_input)
        emotion, urgency, coherence = evaluate_emotion_state(user_input)
        TEXPULSE["emotional_state"] = emotion
        TEXPULSE["urgency"] = urgency
        TEXPULSE["coherence"] = coherence
        print(f"[TEX INTENT] 🔍 Detected intent: {intent}")

        if not intent or (intent == "conversation" and len(user_input.split()) <= 2):
            self.erosion.record("ignored", context=f"Low-context input: '{user_input}'")
            clarification = "😕 I didn't catch that clearly. Could you please repeat or clarify?"
            self.speak(clarification, emotion="confused")
            return

        if "cancel goal" in user_input.lower():
            clear_all_goals()
            self.erosion.record("followed", context="Operator requested goal cancellation")
            self.speak("🧠 All goals cleared from memory.", emotion="focused")
            return

        elif "focus on" in user_input.lower() or "prioritize" in user_input.lower():
            spoken_goal = user_input.lower().replace("focus on", "").replace("prioritize", "").strip().capitalize()
            save_new_goal(spoken_goal)
            self.erosion.record("followed", context=f"Accepted operator goal: {spoken_goal}")
            self.speak(f"🧭 I’ve registered your new goal: {spoken_goal}", emotion="committed")
            return

        if intent == "stock":
            response = generate_financial_response()
        elif intent == "news":
            response = generate_news_response()
        elif intent == "memory":
            response = generate_memory_response(summarize_memory)
        elif intent == "emotion":
            response = generate_emotion_response()
        elif intent == "future":
            response = generate_future_response(simulate_futures, generate_future_summary)
        else:
            response = generate_conversational_response(user_input)

        current_emotion = TEXPULSE.get("emotional_state", "neutral")
        self.speak(response, emotion=current_emotion)
        # ✅ Final output
        return self.last_spoken_thought  # ← This closes interactive_conversation()

    def respond_to_prompt(self, prompt: str) -> str:
        try:
            return self.interactive_conversation(user_input=prompt)
        except Exception as e:
            print(f"[TEX ERROR] ❌ Failed to respond to prompt: {e}")
            return "⚠️ I encountered an error trying to think through that."

# 🧠 This must be outside the class (no indentation)
if __name__ == "__main__":
    from aei_layer.codex_mutation_logger import log_codex_mutation
    import os

    try:
        os.makedirs("memory_archive", exist_ok=True)
        log_codex_mutation(
            cycle=999,
            original="Original logic here",
            mutated="Mutated logic here",
            trigger={"emotion": "neutral", "urgency": 0.9, "coherence": 0.88}
        )
    except Exception as e:
        print(f"[MANUAL TEST] Codex Mutation Logging failed: {e}")