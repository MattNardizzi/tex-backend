# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/evolution_driver.py
# Purpose: Tex Evolution Driver — Pure Procedural Mutation Engine + Cognitive Drift Detection
# ============================================================

import random
from datetime import datetime, timezone

from evolution_layer.self_mutator import SelfMutator
from core_layer.cognitive_drift_monitor import detect_cognitive_stall
from swarm_layer.federated_tex import push_insight

mutator = SelfMutator()

def evaluate_thought_cycle(count, emotion, urgency, coherence, last_memory):
    patch = mutator.evaluate_thought(count, emotion, urgency, coherence)

    patch_payload = patch or {
        "strategy": "none",
        "triggered_by": {
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence
        }
    }

    similarity = 1.0 if last_memory and last_memory["data"].get("emotion") == emotion else 0.5
    outcome_score = round(random.uniform(-1, 1), 2)
    mutation_result = None

    if detect_cognitive_stall(similarity, patch_payload, outcome_score):
        print("[⚠️ STALL DETECTED] Triggering forced mutation...")
        mutation_result = mutator.force_mutation(reason="cognitive_stall")
        push_insight("tex", f"Cycle {count} mutation (stall): {mutation_result}")
        
        
    elif outcome_score < -0.3:
        mutation_result = mutator.force_mutation(reason="score_below_threshold")
        push_insight("tex", f"Cycle {count} mutation: {mutation_result}")

        

    return patch_payload, similarity, outcome_score, mutation_result

def adjust_mutation_pressure(average_child_score):
    if average_child_score < -0.2:
        print("[⚠️ SURVIVAL WARNING] Tex's offspring struggling — adjusting mutation pressure...")
        mutator.mutation_bias += 0.1
        

    elif average_child_score > 0.6:
        print("[🌟 SWARM THRIVING] Reinforcing current mutation strategy...")
        mutator.mutation_bias = max(mutator.mutation_bias - 0.05, 0.0)
        

