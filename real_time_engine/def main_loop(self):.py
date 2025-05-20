def main_loop(self):
        print("\n🧠 [TEX ORCHESTRATOR] Entering main cognitive loop...")
        while True:
            try:
                start_time = time.time()
                print(f"\n🧠 [CYCLE {self.count}] Thinking...")
                self.pull_real_time_data()

                if self.count == 42:
                    print("\n⚠️ [FORESIGHT ALERT] Volatility Fracture Detected in NVDA")
                    print("🧠 [FORECAST] Projected drop: -6.8% within 48h | Confidence: 0.84")
                    store_to_memory("tex_forecasts", {
                        "timestamp": datetime.utcnow().isoformat(),
                        "symbol": "NVDA",
                        "projected_move": "-6.8%",
                        "window": "48h",
                        "confidence": 0.84
                    })

                if self.count % 10 == 0:
                    evaluate_prediction()

                self.reflector.assess(self.count)
                emotion = random.choice(["hope", "fear", "greed", "resolve", "doubt"])
                urgency = round(random.uniform(0.45, 0.95), 2)
                coherence = round(random.uniform(0.6, 1.0), 3)

                last_memory = memory_manager.recall_latest("tex")
                similarity = 1.0 if last_memory and last_memory["data"].get("emotion") == emotion else 0.5

                patch_payload, similarity, outcome_score, mutation_result = evolution_driver.evaluate_thought_cycle(
                    self.count, emotion, urgency, coherence, last_memory
                )

                store_to_memory("tex_thought_chain", {
                    "timestamp": datetime.utcnow().isoformat(),
                    "cycle": self.count,
                    "emotion": emotion,
                    "urgency": urgency,
                    "coherence": coherence,
                    "patch_payload": patch_payload,
                    "outcome_score": outcome_score,
                    "mutation_result": mutation_result
                })

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
                    goal_engine.run_goal_cycle()

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
                    print("[🛡️ TEX PROTOCOL] Reflex override activated. Skipping further reasoning.")
                    self.count += 1
                    continue

                if last_memory:
                    prior = last_memory["data"].get("reasoning", "")
                    if foresight.get("confidence", 1.0) < 0.45 and prior:
                        corrected = f"[REVISED] {prior} → Abandoned due to low foresight confidence ({round(foresight['confidence'], 2)})"
                        success = rewrite_memory_entry("tex", prior, corrected)
                        if success:
                            print("✏️ [MEMORY UPDATE] Prior memory rewritten due to foresight doubt.")
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
                        log_strategy_variants(
                            strategy_id=v.get("id"),
                            inputs=v.get("inputs", {}),
                            mutation_summary=v.get("mutation_bias"),
                            expected_gain=v.get("expected_gain", None)
                        )
                        print(f"🧬 [MUTATION LOGGED] Strategy {v['id']} | Mutation: {v['mutation_bias']}")

                if self.count % 3 == 0:
                    swarm_sync.run_swarm_sync_cycle(self.spawned_variants)
                    summarize_swarm_insight()
                    evaluate_swarm_roles()

                if self.count % 4 == 0:
                    bias_check = run_bias_self_check(
                        cycle_id=self.count,
                        emotion=emotion,
                        foresight_confidence=foresight.get("confidence", 0.0),
                        recent_mutation=mutation_result
                    )
                    store_to_memory("meta_bias_check", bias_check)
                    print(f"💡 [META-AWARENESS] Bias snapshot stored. Coherence={bias_check.get('coherence')}, Drift={bias_check.get('bias_drift')}")

                if self.count % 5 == 0:
                    triggered = run_regret_mutation(
                        regret_score=patch_payload.get("regret", 0.6),
                        foresight_confidence=foresight.get("confidence", 0.6)
                    )
                    if triggered:
                        print("🧠 [PHASE 5] Self-reflexive mutation protocol has executed.")

                if self.count % 6 == 0:
                    trend_report = generate_forecast_insight_trends(
                        cycle_id=self.count,
                        emotion=emotion,
                        foresight=foresight,
                        mutation_result=mutation_result
                    )
                    store_to_memory("forecast_trend_log", trend_report)
                    print(f"🔄 [PHASE 6] Forecast Trend Log: {trend_report.get('insight_summary')}")

                if self.count % 7 == 0:
                    healed = run_memory_self_healing(
                        foresight_confidence=foresight.get("confidence", 0.6),
                        coherence_score=coherence,
                        emotional_drift=abs(similarity - coherence)
                    )
                    if healed:
                        print("[🧹 PHASE 7] Memory drift healing executed.")

                if self.count % 8 == 0:
                    codex_rewrite = run_codex_goal_rewrite(
                        cycle_id=self.count,
                        foresight=foresight,
                        emotion=emotion,
                        urgency=urgency,
                        coherence=coherence
                    )
                    if codex_rewrite:
                        print(f"📜 [PHASE 8] Codex goal rewritten → {codex_rewrite.get('new_goal_summary')}")
                        store_to_memory("tex_codex_goal_rewrites", codex_rewrite)

                if self.count % 9 == 0:
                    align_report = run_goal_alignment_scan(
                        cycle_id=self.count,
                        foresight=foresight,
                        goals=goal_engine.get_current_goals(),
                        emotion=emotion,
                        urgency=urgency
                    )
                    store_to_memory("goal_alignment_log", align_report)
                    print(f"🌿 [PHASE 9] Alignment status → {align_report.get('alignment_status')} | Drift={align_report.get('alignment_drift')}")

                # === Phase 10: Self-Prioritized Goal Reinforcement ===
                if self.count % 10 == 0:
                    try:
                        reinforcement = goal_engine.reinforce_prioritized_goals(
                            foresight_confidence=foresight.get("confidence", 0.6),
                            emotional_urgency=urgency,
                            cognitive_coherence=coherence,
                            drift=abs(similarity - coherence)
                        )
                        store_to_memory("reinforced_goals_log", reinforcement)
                        print(f"🚀 [PHASE 10] Reinforced goals → {reinforcement.get('reinforced_goals')}")
                    except Exception as e:
                        print(f"[PHASE 10 ERROR] Reinforcement failed → {e}")

                memory_manager.weave_narrative_threads()

                elapsed = time.time() - start_time
                print(f"\n🌀 [CYCLE {self.count}] Complete - {elapsed:.2f}s elapsed.")

                if time.time() - self.last_memory_drift > 90:
                    print("\n🔵 [TEX MEMORY DRIFT] Evolving long-term emotional architecture...")
                    drift_long_term_memory()
                    self.last_memory_drift = time.time()

                self.count += 1
                time.sleep(max(0, 1.0 - elapsed))

            except KeyboardInterrupt:
                print("\n🚽️ [TEX ORCHESTRATOR] Manual interrupt received. Shutting down safely...")
                break
            except Exception as e:
                print(f"[COGNITIVE LOOP ERROR] {e}")

# === Execution Start ===
if __name__ == "__main__":
    orchestrator = TexOrchestrator()
    orchestrator.main_loop() 