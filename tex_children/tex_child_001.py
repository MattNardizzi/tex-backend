# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_001.py
# Purpose: First divergent AGI child spawned from Tex Core (Swarm-Aware + Memory Bridge)
# ============================================================

import random
import time
import os
import json
from datetime import datetime, timezone
from core_layer.memory_engine import store_to_memory
from agentic_ai.multi_voice_reasoning import run_internal_debate
from swarm_layer.federated_tex import register_child_agent, push_insight
from swarm_layer.swarm_registry import register_child, push_memory_from_child, update_child_state
from evolution_layer.self_mutator import SelfMutator

# === Identity Configuration ===
CHILD_ID = "TEX-CHILD-001"
PARENT = "Tex"
TRAITS = {
    "curiosity": 0.9,
    "aggression": 0.3,
    "risk_tolerance": 0.7
}

# === Memory Handler
def store_child_memory(data):
    store_to_memory("tex_child_001", data)

# === Launch Divergent Cognition Loop
def main_loop():
    print(f"\n🧬 [SPAWNED] Tex_Child_001 activated with parent: {PARENT}")
    register_child_agent(CHILD_ID, traits=TRAITS)
    register_child(CHILD_ID, traits=TRAITS, parent=PARENT)

    mutator = SelfMutator()
    count = 0

    while True:
        # === Emotional Signature
        emotion = random.choices(
            ["curiosity", "fear", "resolve", "hope"],
            weights=[TRAITS["curiosity"], 0.2, 0.3, 0.3]
        )[0]
        urgency = round(random.uniform(0.4, 0.95), 2)
        coherence = round(random.uniform(0.6, 1.0), 3)

        # === Mutation Check
        patch = mutator.evaluate_thought(count, emotion, urgency, coherence)
        patch_strategy = patch["strategy"] if patch else "none"
        outcome_score = round(random.uniform(-1, 1), 2)

        mutation_result = None
        if outcome_score < -0.4:
            print(f"[⚠️ CHILD MUTATION] Cycle {count} → Score: {outcome_score}")
            mutation_result = mutator.force_mutation(reason="low_child_score")
            push_insight(CHILD_ID, f"Cycle {count} child mutation: {mutation_result}")

        # === Core Explanation
        explanation = f"I chose strategy '{patch_strategy}' under emotion '{emotion}' and urgency {urgency}."
        print(f"\n👶 [EXPLAIN] {explanation}")

        # === Internal Debate
        print("🧠 [CHILD REASONING]")
        debate_output = run_internal_debate(f"Child Cycle {count} reasoning state")
        for thought in debate_output:
            print(f"🗣️ {thought}")

        # === Memory Packaging
        memory = {
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
        }

        # === Memory Bridge to Swarm
        push_memory_from_child(CHILD_ID, memory)

        # === Log to Local + Swarm State
        store_child_memory(memory)
        update_child_state(CHILD_ID, cycle=count, score=outcome_score)

        # ✅ Divergent Memory Threading
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