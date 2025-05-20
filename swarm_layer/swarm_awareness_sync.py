# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_awareness_sync.py
# Purpose: Ingest swarm child memories into Tex Core for recursive evolution
# ============================================================

import os
import json
from datetime import datetime, timezone

SWARM_FEED_PATH = "memory_archive/swarm_feed.jsonl"

# === Load recent swarm child memories
def load_recent_swarm_memories(limit=20):
    if not os.path.exists(SWARM_FEED_PATH):
        return []

    valid_entries = []
    with open(SWARM_FEED_PATH, "r") as f:
        for idx, line in enumerate(f):
            if not line.strip():
                continue
            try:
                entry = json.loads(line.strip())
                if isinstance(entry, dict):  # 🔒 NON-FLAT GUARD
                    valid_entries.append(entry)
                else:
                    print(f"[SWARM FEED WARNING] Skipping non-dict entry at line {idx}")
            except json.JSONDecodeError as e:
                print(f"[SWARM FEED PARSE ERROR] {e} at line {idx}")
                continue

    return valid_entries[-limit:]

# === Summarize and integrate swarm cognition into Tex
def sync_with_swarm_feed():
    memories = load_recent_swarm_memories(limit=30)
    if not memories:
        print("[SWARM SYNC] 🟡 No new child memories found.")
        return

    print(f"[SWARM SYNC] 🧬 Integrating {len(memories)} swarm memories into Tex...")

    survival_emotions = {}
    avg_score = 0
    valid_count = 0

    for entry in memories:
        if not isinstance(entry, dict):  # 🔒 NON-FLAT GUARD
            continue

        agent = entry.get("agent_id", "unknown_child")
        memory = entry.get("memory", {})

        if not isinstance(memory, dict):  # 🔒 NON-FLAT GUARD
            print(f"[SWARM SYNC WARNING] Malformed memory structure for agent {agent}")
            continue

        emotion = memory.get("emotion", "neutral")
        urgency = memory.get("urgency", 0.5)
        score = memory.get("score", 0.0)

        survival_emotions.setdefault(emotion, 0)
        survival_emotions[emotion] += 1
        avg_score += score
        valid_count += 1

    if valid_count > 0:
        avg_score = round(avg_score / valid_count, 3)

    # === Log swarm learning
    print(f"[SWARM SYNC] 🔥 Average Child Cognition Score: {avg_score}")
    print(f"[SWARM SYNC] 💬 Emotional distribution across swarm: {survival_emotions}")

    # === Return analysis (Tex can mutate based on this externally)
    return {
        "average_child_score": avg_score,
        "survival_emotions": survival_emotions,
        "sample_size": valid_count
    }