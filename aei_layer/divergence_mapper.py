# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/divergence_mapper.py
# Purpose: Map fork divergence events from simulated variant paths
# ============================================================

import os
import json
from datetime import datetime

DIVERGENCE_LOG = "memory_archive/divergence_map.jsonl"
os.makedirs("memory_archive", exist_ok=True)

def log_fork_divergence(cycle, fork_id, divergence_score, source_emotion, context=None):
    entry = {
        "cycle": cycle,
        "fork_id": fork_id,
        "divergence_score": round(divergence_score, 4),
        "source_emotion": source_emotion,
        "context": context or {},
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        with open(DIVERGENCE_LOG, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[DIVERGENCE MAP] 🌐 Cycle {cycle} | Fork: {fork_id} → Δ: {divergence_score}")
    except Exception as e:
        print(f"[DIVERGENCE ERROR] {e}")

# === Test
if __name__ == "__main__":
    log_fork_divergence(
        cycle=999,
        fork_id="VARIANT_TEST_123",
        divergence_score=0.712,
        source_emotion="fear",
        context={"variant_bias": "contrarian", "simulated_outcome": "market collapse"}
    )