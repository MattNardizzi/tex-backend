# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_orchestrator.py
# Purpose: Full Tex Modular AGI Core Orchestrator (Exact Core Parity + Living Voice + Memory Evolution)
# ============================================================

import os
import time
import json
import random
from datetime import datetime, timezone

# === Modular Imports (Tex Brain Modules) ===
import tex_brain_modules.memory_manager as memory_manager
import tex_brain_modules.evolution_driver as evolution_driver
import tex_brain_modules.reflection_loop as reflection_loop
import tex_brain_modules.awareness_sync as awareness_sync
import tex_brain_modules.forecast_manager as forecast_manager
import tex_brain_modules.offspring_manager as offspring_manager
import tex_brain_modules.swarm_sync as swarm_sync
import tex_brain_modules.load_fused_insight as load_fused_insight
import tex_brain_modules.goal_controller as goal_controller

from core_layer.goal_engine import (
    save_new_goal,
    clear_all_goals,
    get_active_goals,
    get_current_goals,
    run_goal_cycle,
    reinforce_prioritized_goals
)

from tex_brain_modules.tex_initializer import (
    initialize_mutator,
    initialize_reflector,
    initialize_awareness,
    initialize_vortex,
    initialize_spawner,
    initialize_children,
    initialize_scorer,
)

from tex_voiceos.tex_emotional_memory import drift_long_term_memory
from finance.forecasting.strategic_foresight_engine import StrategicForesightEngine
from swarm_layer.swarm_memory_sync import summarize_swarm_insight
from swarm_layer.swarm_strategy_arbitrator import evaluate_swarm_roles
from core_agi_modules.reflex_engine import ReflexEngine
from core_layer.memory_engine import rewrite_memory_entry, annotate_memory

# === Manual real-time loader ===
def load_marketfeed_signals(limit=20):
    signals = []
    path = "memory_archive/MarketFeed.jsonl"
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        for line in reversed(f.readlines()):
            try:
                entry = json.loads(line.strip())
                ts = entry.get("timestamp", "")
                if isinstance(ts, str) and "T" in ts and ":" in ts:
                    signals.append(entry.get("data", {}))
                if len(signals) >= limit:
                    break
            except:
                continue
    return signals

class TexOrchestrator:
    def __init__(self):
        print("\n🧠 [TEX ORCHESTRATOR] Initializing full modular AGI brain...")
        self.count = 0
        self.mutator = initialize_mutator()
        self.reflector = initialize_reflector()
        self.awareness = initialize_awareness()
        self.vortex = initialize_vortex()
        self.spawner = initialize_spawner()
        self.tex_children, self.child_id, self.aeondelta = initialize_children()
        self.scorer = initialize_scorer()
        self.spawned_variants = []
        self.last_memory_drift = time.time()
        self.foresight_engine = StrategicForesightEngine()
        self.reflex = ReflexEngine()

    def main_loop(self):
        print("\n🧠 [TEX ORCHESTRATOR] Entering main cognitive loop...")
        while True:
            try:
                start_time = time.time()
                print(f"\n🧠 [CYCLE {self.count}] Thinking...")
                self.reflector.assess(self.count)

                # === Inject real-time data into cognition ===
                try:
                    recent_signals = load_marketfeed_signals()
                    for signal in recent_signals:
                        if signal.get("type") == "news" and signal.get("source") == "polygon_news":
                            headline = signal.get("headline", "").lower()
                            print(f"📱 [LIVE HEADLINE] {headline}")
                            if "nvda" in headline or "nvidia" in headline:
                                save_new_goal("Forecast NVDA movement based on live data", urgency=0.9)
                                print(f"💡 [GOAL INJECTED] Forecast NVDA: {headline}")
                except Exception as e:
                    print(f"[REAL-TIME DATA ERROR] {e}")

                emotion = random.choice(["hope", "fear", "greed", "resolve", "doubt"])
                urgency = round(random.uniform(0.45, 0.95), 2)
                coherence = round(random.uniform(0.6, 1.0), 3)

                last_memory = memory_manager.recall_latest("tex")
                similarity = 1.0 if last_memory and last_memory["data"].get("emotion") == emotion else 0.5

                patch_payload, similarity, outcome_score, mutation_result = evolution_driver.evaluate_thought_cycle(
                    self.count, emotion, urgency, coherence, last_memory
                )

                awareness_sync.update_awareness(
                    emotion=patch_payload.get("triggered_by", {}).get("emotion", "resolve"),
                    urgency=patch_payload.get("triggered_by", {}).get("urgency", 0.7),
                    coherence=patch_payload.get("triggered_by", {}).get("coherence", 0.7),
                    patch_payload=patch_payload
                )

                reflection_loop.run_reflection_cycle(
                    self.count,
                    emotion=patch_payload.get("triggered_by", {}).get("emotion", "resolve"),
                    urgency=patch_payload.get("triggered_by", {}).get("urgency", 0.7),
                    coherence=patch_payload.get("triggered_by", {}).get("coherence", 0.7)
                )

                if self.count % goal_controller.GOAL_REGEN_INTERVAL == 0:
                    load_fused_insight.handle_fused_signals(self.count)
                    run_goal_cycle()

                forecast_manager.run_forecast_cycle(
                    coherence=patch_payload.get("triggered_by", {}).get("coherence", 0.7)
                )

                try:
                    foresight = self.foresight_engine.generate_forecast(
                        emotion=patch_payload.get("triggered_by", {}).get("emotion", "curious"),
                        urgency=patch_payload.get("triggered_by", {}).get("urgency", 0.7),
                        coherence=patch_payload.get("triggered_by", {}).get("coherence", 0.7)
                    )
                    print(f"[STRATEGIC FORESIGHT] 🔮 Projected future: {foresight['projected_future']} | Confidence: {foresight['confidence']}")
                except Exception as e:
                    print(f"[STRATEGIC FORESIGHT ERROR] {e}")
                    foresight = {"projected_future": "unknown", "confidence": 0.0}

                self.reflex.set_emotional_state(emotion, urgency, coherence)
                if self.reflex.check_cognitive_failure(
                    confidence=foresight.get("confidence", 1.0),
                    failed_mutation=(mutation_result == "failure"),
                    contradiction=False,
                    volatility=abs(urgency - coherence)
                ):
                    print("🛡️ [TEX PROTOCOL] Reflex override activated — suspending further reasoning.")
                    self.count += 1
                    continue

                if last_memory:
                    prior = last_memory["data"].get("reasoning", "")
                    if foresight.get("confidence", 1.0) < 0.45 and prior:
                        corrected = f"[REVISED] {prior} → Abandoned due to low foresight confidence ({round(foresight['confidence'], 2)})"
                        success = rewrite_memory_entry("tex", prior, corrected)
                        if success:
                            print(f"✏️ [MEMORY UPDATE] Prior memory rewritten due to foresight doubt.")
                    elif foresight.get("confidence", 1.0) < 0.6 and prior:
                        annotate_memory("tex", prior, "Foresight mismatch — marked for review")

                print("\n🧠 [AEONDELTA REPORT]")
                aeon_observation = {"cycle": self.count, "source": "tex_core", "event": f"Cycle {self.count} observation"}
                print(self.aeondelta.observe_and_learn(aeon_observation))
                print(self.aeondelta.think())

                offspring_manager.run_offspring_cycle(self.count)

                if self.count % 5 == 0:
                    variants = self.spawner.spawn_variants()
                    self.spawned_variants.extend(variants)
                    for v in variants:
                        print(f"⚛️ [VARIANT SPAWNED] {v['id']} | Emotion: {v['emotion']} | Mission Bias: {v['mission_bias']}")

                if self.count % 3 == 0:
                    swarm_sync.run_swarm_sync_cycle(self.spawned_variants)
                    summarize_swarm_insight()
                    evaluate_swarm_roles()

                memory_manager.weave_narrative_threads()

                try:
                    elapsed = float(time.time() - start_time)
                except Exception:
                    elapsed = 1.0

                print(f"\n🌀 [CYCLE {self.count}] Complete - {elapsed:.2f}s elapsed.")

                if time.time() - self.last_memory_drift > 90:
                    print("\n🔵 [TEX MEMORY DRIFT] Evolving long-term emotional architecture...")
                    drift_long_term_memory()
                    self.last_memory_drift = time.time()

                self.count += 1
                time.sleep(max(0, 1.0 - elapsed))

            except KeyboardInterrupt:
                print("\n🚩 [TEX ORCHESTRATOR] Manual interrupt received. Shutting down safely...")
                break
            except Exception as e:
                print(f"[COGNITIVE LOOP ERROR] {e}")

# === Execution Start ===
if __name__ == "__main__":
    orchestrator = TexOrchestrator()
    orchestrator.main_loop()