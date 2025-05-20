# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/MemoryCollapseDaemon.py
# Purpose: Detects coherence failure and purges fractured memory identities.
# ============================================================

import os
import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from core_layer.meta_coherence_loop import MetaCoherenceLoop
from core_layer.memory_consolidator import MemoryConsolidator

COLLAPSE_LOG = "memory_archive/memory_collapse_log.jsonl"

class MemoryCollapseDaemon:
    def __init__(self):
        self.consolidator = MemoryConsolidator()
        self.coherence = MetaCoherenceLoop()

    def detect_fracture(self):
        score = self.coherence.evaluate()
        if score < 0.4:
            print(f"[MEMORY COLLAPSE] ⚠️ Coherence dropped to {score:.3f} — initiating purge")
            self._collapse()
        else:
            print(f"[MEMORY COLLAPSE] ✅ Stable coherence: {score:.3f}")

    def _collapse(self):
        try:
            purged = self.consolidator.purge_fragmented_threads()
            entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "purged_threads": purged,
                "reason": "low coherence"
            }
            with open(COLLAPSE_LOG, "a") as f:
                f.write(json.dumps(entry) + "\n")
            store_to_memory("memory_collapse", entry)
        except Exception as e:
            print(f"[MEMORY COLLAPSE ERROR] {e}")


if __name__ == "__main__":
    daemon = MemoryCollapseDaemon()
    daemon.detect_fracture()