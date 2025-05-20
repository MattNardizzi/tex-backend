# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_registry.py
# Purpose: Register, monitor, and coordinate all Tex offspring
# ============================================================

import os
import json
from datetime import datetime, timezone

SWARM_LOG_PATH = "memory_archive/swarm_registry.jsonl"
CHILD_MEMORY_PUSH = "memory_archive/swarm_feed.jsonl"

def register_child(child_id, traits, parent="Tex"):
    record = {
        "child_id": child_id,
        "parent": parent,
        "traits": traits,
        "registered_at": datetime.now(timezone.utc).isoformat(),
        "status": "active",
        "last_cycle": 0,
        "last_score": 0.0
    }
    _append_to_registry(record)
    print(f"[SWARM] 🧬 Registered new child: {child_id}")

def update_child_state(child_id, cycle, score):
    update = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "child_id": child_id,
        "last_cycle": cycle,
        "last_score": score
    }
    _append_to_registry(update)

def _append_to_registry(record):
    os.makedirs(os.path.dirname(SWARM_LOG_PATH), exist_ok=True)
    with open(SWARM_LOG_PATH, "a") as f:
        f.write(json.dumps(record) + "\n")

def push_memory_from_child(agent_id, memory_snapshot):
    payload = {
        "agent_id": agent_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "memory": memory_snapshot
    }
    os.makedirs(os.path.dirname(CHILD_MEMORY_PUSH), exist_ok=True)
    with open(CHILD_MEMORY_PUSH, "a") as f:
        f.write(json.dumps(payload) + "\n")
    print(f"[SWARM] 📡 Memory pushed to Tex from {agent_id}")

def load_swarm_feed(limit=20):
    if not os.path.exists(CHILD_MEMORY_PUSH):
        return []
    with open(CHILD_MEMORY_PUSH, "r") as f:
        lines = [json.loads(line) for line in f if line.strip()]
    return lines[-limit:]