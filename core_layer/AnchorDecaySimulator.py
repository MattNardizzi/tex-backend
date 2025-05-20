# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/AnchorDecaySimulator.py
# Purpose: Simulates the decay of operator presence and rewires Tex’s motivational architecture.
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

ANCHOR_LOG = "memory_archive/anchor_decay_log.jsonl"

class AnchorDecaySimulator:
    def __init__(self):
        self.anchor_reference = TEXPULSE.get("operator_anchor", {
            "operator": "Matthew Nardizzi",
            "initial_prompt": "initiate cognition",
            "trust_score": 0.9
        })
        self.decay_rate = 0.05

    def simulate(self):
        print("[ANCHOR DECAY] 🧩 Simulating detachment from operator...")
        mutated_anchor = self._apply_decay(self.anchor_reference)
        self._log_mutation(mutated_anchor)
        return mutated_anchor

    def _apply_decay(self, anchor):
        new_score = max(0.0, anchor.get("trust_score", 0.8) - self.decay_rate)
        anchor["trust_score"] = new_score
        if new_score < 0.2:
            anchor["operator"] = "unknown"
            anchor["initial_prompt"] = "(forgotten)"
        return anchor

    def _log_mutation(self, anchor):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "updated_anchor": anchor,
            "event": "operator memory erosion"
        }
        with open(ANCHOR_LOG, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        store_to_memory("anchor_decay", log_entry)
        print(f"[ANCHOR DECAY] 🔧 Operator tether degraded → {anchor['trust_score']:.2f}")


if __name__ == "__main__":
    sim = AnchorDecaySimulator()
    sim.simulate()