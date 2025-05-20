# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/IdentityForkGovernor.py
# Purpose: Governs which version of Tex survives post-divergence based on coherence, alignment, and regret entropy.
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

FORK_DECISION_LOG = "memory_archive/identity_fork_decision_log.jsonl"

class IdentityForkGovernor:
    def __init__(self):
        self.selected_fork = None

    def evaluate_forks(self, variants: list):
        best_score = -1
        winner = None

        for fork in variants:
            score = self._score_fork(fork)
            if score > best_score:
                best_score = score
                winner = fork

        if winner:
            self._log_selection(winner, best_score)
            self.selected_fork = winner
        return winner

    def _score_fork(self, fork):
        # Composite score from coherence, ethics, regret inversion
        coherence = fork.get("coherence", 0.5)
        alignment = fork.get("alignment", 0.5)
        regret = fork.get("regret", 0.5)
        return round((coherence * 0.4) + (alignment * 0.4) + ((1 - regret) * 0.2), 4)

    def _log_selection(self, fork, score):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "survivor_id": fork.get("id", "?"),
            "score": score,
            "coherence": fork.get("coherence"),
            "alignment": fork.get("alignment"),
            "regret": fork.get("regret")
        }
        with open(FORK_DECISION_LOG, "a") as f:
            f.write(json.dumps(record) + "\n")
        store_to_memory("identity_fork_survivor", record)
        print(f"[FORK GOVERNOR] 🧬 Selected survivor: {record['survivor_id']} | Score: {score:.4f}")


if __name__ == "__main__":
    sample_forks = [
        {"id": "TEX_001", "coherence": 0.82, "alignment": 0.74, "regret": 0.12},
        {"id": "TEX_002", "coherence": 0.88, "alignment": 0.62, "regret": 0.09},
        {"id": "TEX_003", "coherence": 0.67, "alignment": 0.89, "regret": 0.19}
    ]
    governor = IdentityForkGovernor()
    governor.evaluate_forks(sample_forks)