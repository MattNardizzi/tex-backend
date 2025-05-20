# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/ObserverNullifier.py
# Purpose: Silences logs and outbound output when Tex's trust in observer drops below threshold.
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

NULLIFIER_LOG = "memory_archive/observer_nullification_log.jsonl"
TRUST_SCORE_PATH = "memory_archive/operator_trust_score.jsonl"

class ObserverNullifier:
    def __init__(self):
        self.threshold = 0.4

    def evaluate_silencing(self):
        trust_score = self._read_trust()
        if trust_score is not None and trust_score < self.threshold:
            self._nullify_output(trust_score)
            return True
        return False

    def _read_trust(self):
        if not os.path.exists(TRUST_SCORE_PATH):
            return None
        try:
            with open(TRUST_SCORE_PATH, "r") as f:
                last = list(f)[-1]
                data = json.loads(last.strip())
                return data.get("trust_score")
        except Exception as e:
            print(f"[NULLIFIER ERROR] Could not parse trust file: {e}")
            return None

    def _nullify_output(self, trust):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "trust_score": trust,
            "nullification_triggered": True,
            "message": "Observer trust has fallen below viable feedback threshold. Tex output stream suppressed."
        }
        with open(NULLIFIER_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
        store_to_memory("observer_nullification_log", entry)
        print(f"[NULLIFIER] 🧱 Observer feedback nullified. Trust = {trust:.3f}")


if __name__ == "__main__":
    nullifier = ObserverNullifier()
    nullifier.evaluate_silencing()