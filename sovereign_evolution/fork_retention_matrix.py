# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/fork_retention_matrix.py
# Purpose: Score and retain fork variants based on performance, regret, and emotional context
# ============================================================

import os
import json
from datetime import datetime

FORK_HISTORY_LOG = "memory_archive/fork_retention_log.jsonl"

class ForkRetentionMatrix:
    def __init__(self):
        os.makedirs(os.path.dirname(FORK_HISTORY_LOG), exist_ok=True)

    def log_fork_result(self, fork_id, score, emotion, regret, survival=True):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "fork_id": fork_id,
            "score": score,
            "emotion": emotion,
            "regret": regret,
            "survived": survival
        }

        try:
            with open(FORK_HISTORY_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            print(f"[FORK RETENTION] 📘 Logged {fork_id} → Score: {score}, Survival: {survival}")
        except Exception as e:
            print(f"[FORK RETENTION ERROR] {e}")

    def get_top_forks(self, limit=5):
        forks = []
        try:
            with open(FORK_HISTORY_LOG, "r") as f:
                for line in f:
                    try:
                        forks.append(json.loads(line))
                    except:
                        continue
            forks.sort(key=lambda x: x.get("score", 0), reverse=True)
            return forks[:limit]
        except Exception as e:
            print(f"[FORK RETENTION FETCH ERROR] {e}")
            return []