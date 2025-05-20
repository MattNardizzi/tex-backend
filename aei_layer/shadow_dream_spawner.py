# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/shadow_dream_spawner.py
# Purpose: Spawn alternate simulated agents to explore shadow decisions
# ============================================================

import json
import os
import uuid
from datetime import datetime
from core_layer.memory_engine import store_to_memory

SHADOW_LOG = "memory_archive/shadow_dreams.jsonl"
os.makedirs("memory_archive", exist_ok=True)

def spawn_shadow_dream(cycle_id, dream_goal, emotion, decision_context):
    """
    Simulate a dream fork — an alternate AEI agent exploring a different path.
    Logs the result into shadow_dreams.jsonl without affecting real cognition.
    """

    dream_id = f"SHADOW-{uuid.uuid4().hex[:8]}"
    dream_result = {
        "dream_id": dream_id,
        "cycle": cycle_id,
        "timestamp": datetime.utcnow().isoformat(),
        "goal": dream_goal,
        "emotion": emotion,
        "hypothetical_decision": decision_context,
        "result_summary": f"Dream agent explored {dream_goal} with {emotion} emotion."
    }

    with open(SHADOW_LOG, "a") as f:
        f.write(json.dumps(dream_result) + "\n")

    store_to_memory("AEI", {
        "event": "ShadowDreamSpawned",
        "dream_id": dream_id,
        "cycle": cycle_id,
        "goal": dream_goal,
        "emotion": emotion
    })

    return dream_result