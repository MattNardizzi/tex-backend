# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_children/tex_child_002.py
# Purpose: Second divergent AGI child spawned from Tex Core (Wrapped in Class)
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

class TexChild002:
    def __init__(self):
        self.child_id = "TEX-CHILD-002"
        self.parent = "Tex"
        self.traits = {
            "curiosity": 0.3,
            "aggression": 0.85,
            "risk_tolerance": 0.9
        }
        self.mutator = SelfMutator()
        self.count = 0

    def store_child_memory(self, data):
        store_to_memory("tex_child_002", data)

    def launch_cognition(self):
        print(f"\n🧬 [SPAWNED] {self.child_id} activated with parent: {self.parent}")
        register_child_agent(self.child_id, traits=self.traits)

        while True:
            emotion = random.choices(
                ["aggression", "fear", "resolve", "hope"],
                weights=[self.traits["aggression"], 0.2, 0.4, 0.2]
            )[0]
            urgency = round(random.uniform(0.5, 0.95), 2)
            coherence = round(random.uniform(0.5, 1.0), 3)

            patch = self.mutator.evaluate_thought(self.count, emotion, urgency, coherence)
            patch_strategy = patch["strategy"] if patch else "none"
            outcome_score = round(random.uniform(-1, 1), 2)

            mutation_result = None
            if outcome_score < -0.3:
                print(f"[⚠️ CHILD MUTATION] Cycle {self.count} → Score: {outcome_score}")
                mutation_result = self.mutator.force_mutation(reason="low_child_score")
                push_insight(self.child_id, f"Cycle {self.count} child mutation: {mutation_result}")

            explanation = f"I chose strategy '{patch_strategy}' under emotion '{emotion}' and urgency {urgency}."
            print(f"\n👶 [EXPLAIN] {explanation}")
            print("🦰 [CHILD REASONING]")
            debate_output = run_internal_debate(f"Child Cycle {self.count} reasoning state")
            for thought in debate_output:
                print(f"🗣️ {thought}")

            # === Core Memory Store
            self.store_child_memory({
                "cycle": self.count,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "agent": self.child_id,
                "parent": self.parent,
                "emotion": emotion,
                "urgency": urgency,
                "coherence": coherence,
                "score": outcome_score,
                "explanation": explanation,
                "mutation_applied": mutation_result if mutation_result else "none",
                "debate_summary": debate_output
            })

            # ✅ Divergent Threaded Memory
            store_to_memory(f"{self.child_id}_memory", {
                "timestamp": datetime.utcnow().isoformat(),
                "cycle": self.count,
                "emotion": emotion,
                "score": outcome_score,
                "reasoning": explanation,
                "debate": debate_output
            })

            self.count += 1
            time.sleep(3)

# === CLI Entry Point ===
if __name__ == "__main__":
    child = TexChild002()
    child.launch_cognition()