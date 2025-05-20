# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/auto_fork_heuristics.py
# Purpose: Score forks and reinforce successful mutations across cycles
# ============================================================

import json
import os
from datetime import datetime

FORK_LOG = "memory_archive/strategy_mutations.jsonl"
SCORED_LOG = "memory_archive/fork_performance_scores.jsonl"

class AutoForkHeuristics:
    def __init__(self):
        os.makedirs(os.path.dirname(SCORED_LOG), exist_ok=True)

    def score_fork(self, fork):
        """
        Score a fork's utility based on its emotional alignment and result impact.
        You can later evolve this into a neural scoring model.
        """
        emotion = fork.get("emotion", "neutral")
        regret = fork.get("regret", 0.5)
        gain = fork.get("performance_gain", 0.0)
        confidence = fork.get("confidence", 0.5)

        # Weighted scoring model (tune as needed)
        score = round(
            0.4 * (1.0 - regret) +
            0.3 * gain +
            0.2 * confidence +
            0.1 * (1.0 if emotion == "resolve" else 0.0),
        3)

        packet = {
            "timestamp": datetime.utcnow().isoformat(),
            "fork_id": fork.get("id", "unknown"),
            "emotion": emotion,
            "regret": regret,
            "gain": gain,
            "confidence": confidence,
            "score": score
        }

        with open(SCORED_LOG, "a") as f:
            f.write(json.dumps(packet) + "\n")

        print(f"[FORK HEURISTICS] 🔁 Scored fork {packet['fork_id']} → {score}")
        return score