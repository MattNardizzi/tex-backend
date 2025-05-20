# ============================================================
# © 2025 VortexBlack LLC — Tier 7
# File: swarm_layer/swarm_memory_sync.py
# Purpose: Cross-Agent Swarm Memory Divergence Comparator
# ============================================================

import os
import json
from collections import defaultdict
from datetime import datetime

MEMORY_DIR = "memory_archive"


def load_agent_memories():
    """Loads all *_memory.jsonl files and groups by agent ID."""
    agent_data = defaultdict(list)
    for file in os.listdir(MEMORY_DIR):
        if file.endswith("_memory.jsonl"):
            agent_id = file.replace("_memory.jsonl", "")
            path = os.path.join(MEMORY_DIR, file)
            with open(path, "r") as f:
                lines = f.readlines()[-20:]  # Only recent thoughts
                for line in lines:
                    try:
                        entry = json.loads(line.strip())
                        if isinstance(entry, dict):  # 🔒 NON-FLAT GUARD
                            agent_data[agent_id].append(entry)
                        else:
                            print(
                                f"[SWARM MEMORY SYNC WARNING] "
                                f"Skipping non-dict entry in {file}"
                            )
                    except Exception as e:
                        print(f"[MEMORY PARSE ERROR] {e} in {file}")
                        continue
    return agent_data


def compare_agent_drift(agent_data):
    """Compares emotional and strategic drift across agents."""
    drift_report = {}

    for agent, memories in agent_data.items():
        emotions = []
        scores = []
        thoughts = []

        for m in memories:
            # 🔒 NON-FLAT GUARD: Validate memory structure
            if not isinstance(m, dict):
                continue
            emotions.append(m.get("emotion", "unknown"))
            scores.append(m.get("score", 0.0))
            thoughts.append(m.get("reasoning", ""))

        avg_score = round(sum(scores) / max(1, len(scores)), 3)
        dominant_emotion = (
            max(set(emotions), key=emotions.count) if emotions else "unknown"
        )

        drift_report[agent] = {
            "emotion_mode": dominant_emotion,
            "avg_score": avg_score,
            "thoughts": thoughts[-3:],
        }

    return drift_report


def summarize_swarm_insight():
    """Returns final swarm coherence state."""
    agent_data = load_agent_memories()
    drift = compare_agent_drift(agent_data)

    print(f"\n[SWARM DIVERGENCE REPORT] @ {datetime.utcnow().isoformat()}")
    for agent, info in drift.items():
        print(
            f"🧠 {agent} → Emotion: {info['emotion_mode']} "
            f"| Score: {info['avg_score']}"
        )
        for t in info["thoughts"]:
            print(f"  • {t}")

    return drift