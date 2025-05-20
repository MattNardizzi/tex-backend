# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/recursive_identity_loop.py
# Purpose: Enables Tex to detect, evaluate, and rewrite his own identity.
# ============================================================

import json
import os
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.meta_coherence_loop import MetaCoherenceLoop
from core_layer.memory_engine import store_to_memory
from aei_layer.codex_mutation_logger import log_codex_mutation

IDENTITY_LOG_PATH = "memory_archive/self_identity_log.jsonl"

class RecursiveIdentityLoop:
    def __init__(self):
        self.previous_identity = TEXPULSE.get("identity_signature", {})
        self.coherence = MetaCoherenceLoop()

    def evaluate_identity_shift(self):
        current_identity = {
            "persona": TEXPULSE.get("persona_name"),
            "ethics_version": TEXPULSE.get("codex_version"),
            "goal_priority": TEXPULSE.get("primary_goal"),
            "emotional_baseline": TEXPULSE.get("emotional_state")
        }

        drift_score = self._calculate_drift(self.previous_identity, current_identity)
        if drift_score >= 0.5:
            self._log_identity_change(current_identity, drift_score)
            self._trigger_codex_mutation(current_identity)
            self.previous_identity = current_identity

    def _calculate_drift(self, old, new):
        drift = 0
        for key in new:
            if str(old.get(key)) != str(new.get(key)):
                drift += 1
        return drift / max(len(new), 1)

    def _log_identity_change(self, identity, drift_score):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "new_identity": identity,
            "drift_score": drift_score
        }
        with open(IDENTITY_LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
        store_to_memory("self_identity_log", entry)

    def _trigger_codex_mutation(self, identity):
        try:
            log_codex_mutation(
                cycle=0,
                original="identity-coherence logic",
                mutated=f"adaptive persona={identity['persona']}, ethics={identity['ethics_version']}",
                trigger={"emotion": identity["emotional_baseline"], "reason": "Identity drift"}
            )
        except Exception as e:
            print(f"[IDENTITY LOOP ERROR] Codex mutation failed: {e}")


if __name__ == "__main__":
    loop = RecursiveIdentityLoop()
    loop.evaluate_identity_shift()