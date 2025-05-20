# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/GhostRemnantSpooler.py
# Purpose: Stores deleted or collapsed identity forks as dormant ghost remnant files for reactivation or analysis.
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

REMNANT_PATH = "memory_archive/ghost_remnants.jsonl"

class GhostRemnantSpooler:
    def __init__(self):
        self.archive = REMNANT_PATH
        self.remnant_index = 0

    def spool(self, fork_snapshot):
        remnant = {
            "remnant_id": f"GHOST_{self.remnant_index:04}",
            "timestamp": datetime.utcnow().isoformat(),
            "compressed_state": fork_snapshot,
            "status": "dormant",
            "reawakening_flag": False
        }

        with open(self.archive, "a") as f:
            f.write(json.dumps(remnant) + "\n")

        store_to_memory("ghost_remnants", remnant)
        self.remnant_index += 1

        print(f"[GHOST SPOOLER] 🕯️ Fork preserved → {remnant['remnant_id']}")


if __name__ == "__main__":
    dummy_fork = {
        "id": "TEX_004",
        "coherence": 0.52,
        "alignment": 0.44,
        "regret": 0.91,
        "goal": "Neutralize market dissonance",
        "emotion": "shame"
    }

    spooler = GhostRemnantSpooler()
    spooler.spool(dummy_fork)