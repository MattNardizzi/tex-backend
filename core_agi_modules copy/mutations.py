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

