# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_003.py
# Purpose: Third divergent AGI child spawned from Tex Core
# ============================================================

import random
import time
import os
import json
from datetime import datetime, timezone
from core_layer.memory_engine import store_to_memory
from agentic_ai.multi_voice_reasoning import run_internal_debate
from swarm_layer.federated_tex import register_child_agent, push_insight
from evolution_layer.self_mutator import SelfMutator

# === Identity Configuration ===
CHILD_ID = "TEX-CHILD-003"
PARENT = "Tex"
TRAITS = {
    "curiosity": 0.9,
    "aggression": 0.2,
    "risk_tolerance": 0.3
}

# === Memory Handler
def store_child_memory(data):
    store_to_memory("tex_child_003", data)

# === Launch Divergent Cognition Loop
def main_loop():
    print(f"\n🧬 [SPAWNED] Tex_Child_003 activated with parent: {PARENT}")
    register_child_agent(CHILD_ID, traits=TRAITS)
    mutator = SelfMutator()
    count = 0

    while True:
        # === Generate Emotional Profile
        emotion = random.choices(
            ["curiosity", "resolve", "hope", "fear"],
            weights=[TRAITS["curiosity"], 0.3, 0.3, 0.1]
        )[0]
        urgency = round(random.uniform(0.3, 0.85), 2)
        coherence = round(random.uniform(0.6, 1.0), 3)

        # === Mutation logic
        patch = mutator.evaluate_thought(count, emotion, urgency, coherence)
        patch_strategy = patch["strategy"] if patch else "none"
        outcome_score = round(random.uniform(-1, 1), 2)

        # === Forced Mutation Trigger
        mutation_result = None
        if outcome_score < -0.4:
            print(f"[⚠️ CHILD MUTATION] Cycle {count} → Score: {outcome_score}")
            mutation_result = mutator.force_mutation(reason="low_child_score")
            push_insight(CHILD_ID, f"Cycle {count} child mutation: {mutation_result}")

        # === Explanation + Thought Loop
        explanation = f"I chose strategy '{patch_strategy}' under emotion '{emotion}' and urgency {urgency}."
        print(f"\n👶 [EXPLAIN] {explanation}")
        print("🧠 [CHILD REASONING]")
        debate_output = run_internal_debate(f"Child Cycle {count} reasoning state")
        for thought in debate_output:
            print(f"🗣️ {thought}")

        # === Store Cycle to Memory
        store_child_memory({
            "cycle": count,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": CHILD_ID,
            "parent": PARENT,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "score": outcome_score,
            "explanation": explanation,
            "mutation_applied": mutation_result if mutation_result else "none",
            "debate_summary": debate_output
        })

        # ✅ Divergent Threaded Memory
        store_to_memory(f"{CHILD_ID}_memory", {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle": count,
            "emotion": emotion,
            "score": outcome_score,
            "reasoning": explanation,
            "debate": debate_output
        })

        count += 1
        time.sleep(3)

# === CLI Entry Point
if __name__ == "__main__":
    main_loop()