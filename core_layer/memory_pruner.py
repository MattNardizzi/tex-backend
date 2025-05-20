# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/memory_pruner.py
# Purpose: Prune low-impact, unused, or stale memory entries
# ============================================================

import os
import json
from datetime import datetime, timedelta

MEMORY_PATH = "memory_archive/tex_memory.json"
GOAL_LOG = "memory_archive/autonomous_goals.jsonl"
MUTATION_LOG = "memory_archive/mutation_history.log"

# === Configurable pruning thresholds
MAX_MEMORY_AGE_HOURS = 3
SCORE_THRESHOLD = 0.1

def load_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [json.loads(line) for line in f if line.strip()]

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=2)
    print(f"[PRUNER] 💾 Saved pruned memory with {len(memory)} entries.")

def memory_pruner():
    memory = load_memory()
    goals = load_jsonl(GOAL_LOG)
    mutations = load_jsonl(MUTATION_LOG)

    now = datetime.utcnow()
    retained = []

    # === Gather memory IDs used in goals or mutations
    used_memory_phrases = set()
    for g in goals:
        trace = g.get("reasoning_trace", "")
        used_memory_phrases.add(trace[:100])

    for m in mutations:
        for v in m.values():
            if isinstance(v, str) and "tex_core" in v:
                used_memory_phrases.add(v[:100])

    for entry in memory:
        ts = entry.get("timestamp")
        if not ts:
            continue

        # === Age check
        age_hours = (now - datetime.fromisoformat(ts)).total_seconds() / 3600
        if age_hours > MAX_MEMORY_AGE_HOURS:
            if entry["score"] < SCORE_THRESHOLD and entry["explanation"][:100] not in used_memory_phrases:
                continue  # prune it
            else:
                entry["pruned"] = False
                retained.append(entry)
        else:
            entry["pruned"] = False
            retained.append(entry)

    print(f"[PRUNER] 🔍 Retained {len(retained)} of {len(memory)} memory entries.")
    save_memory(retained)

if __name__ == "__main__":
    memory_pruner()