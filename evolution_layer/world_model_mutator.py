# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: evolution_layer/world_model_mutator.py
# Purpose: Mutate Tex's strategy if worldview diverges from reality
# ============================================================

import os
import json
from datetime import datetime, timezone
from evolution_layer.self_mutator import SelfMutator
from swarm_layer.federated_tex import push_insight

WORLD_MODEL_LOG = "memory_archive/world_model_log.jsonl"
DRIFT_THRESHOLD = 0.6
MIN_ENTRIES = 10

def assess_world_model_drift():
    if not os.path.exists(WORLD_MODEL_LOG):
        print("[DRIFT] 🌍 No world model log found.")
        return

    with open(WORLD_MODEL_LOG, "r") as f:
        lines = [json.loads(line) for line in f if line.strip()]

    if len(lines) < MIN_ENTRIES:
        print(f"[DRIFT] 📉 Not enough belief entries ({len(lines)}) to assess drift.")
        return

    recent = lines[-25:]
    errors = []
    for entry in recent:
        pred = entry.get("prediction", "").lower()
        actual = entry.get("actual", "").lower()
        error = 1.0 if pred != actual else 0.0  # Simple mismatch
        errors.append(error)

    drift_score = round(sum(errors) / len(errors), 2)

    print(f"[DRIFT] 📊 Drift Score = {drift_score} over last {len(recent)} predictions.")

    if drift_score > DRIFT_THRESHOLD:
        print("[DRIFT] ⚠️ Drift threshold exceeded. Triggering worldview mutation...")
        mutator = SelfMutator()
        result = mutator.force_mutation(reason="world_model_drift")

        insight = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source": "world_model_mutator",
            "event": "belief_drift_mutation",
            "drift_score": drift_score,
            "mutation_result": result
        }

        push_insight("tex", insight)
        print(f"[DRIFT] 🔥 Pushed mutation insight due to worldview divergence.")