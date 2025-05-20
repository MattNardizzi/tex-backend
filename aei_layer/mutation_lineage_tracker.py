# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/mutation_lineage_tracker.py
# Purpose: Track strategic mutations and fork lineage for AEI logic
# ============================================================

import json
import os
from datetime import datetime, timezone

LINEAGE_LOG_PATH = "memory_archive/mutation_history.jsonl"

def log_mutation_lineage(cycle, variant_id, mutation_type, gain, emotion="neutral"):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cycle": cycle,
        "variant_id": variant_id,
        "mutation_type": mutation_type,
        "performance_gain": gain,
        "emotion": emotion
    }
    
    try:
        with open(LINEAGE_LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[MUTATION LOG] 🧬 Mutation recorded → {variant_id} | Gain: {gain}")
    except Exception as e:
        print(f"[MUTATION LINEAGE ERROR] {e}")

if __name__ == "__main__":
    print("🔬 Running manual mutation history test...")
    test_data = {
        "variant_id": "TEST_VARIANT_XYZ",
        "cycle": 999,
        "mutation_type": "test_injection",
        "gain": 0.07,
        "emotion": "curiosity"
    }
    log_mutation_lineage(**test_data)