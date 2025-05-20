# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/breathing_loop.py
# Purpose: Exact copy of start_breathing_cycle() from tex_conversational_brain.py
# ============================================================

import time
import threading
import json

from core_layer.tex_manifest import TEXPULSE
from core_layer.goal_engine import get_active_goals
from aei_layer.shadow_dream_spawner import spawn_shadow_dream
from aei_layer.ethics_codex_refiner import refine_codices
from aei_layer.internal_debate_chamber import run_internal_debate
from aei_layer.bias_awareness_monitor import monitor_bias_drift
from aei_layer.self_healing_memory_engine import self_heal_memory
from aei_layer.divergence_mapper import log_fork_divergence
from core_layer.memory_weaver import weave_narrative_threads
from core_agi_modules.reasoning_fragments import think, generate_reasoned_speech
from core_agi_modules.decide_to_speak import decide_to_speak
from dream_layer.dream_simulator import trigger_dream_simulation

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