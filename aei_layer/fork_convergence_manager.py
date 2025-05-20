# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/fork_convergence_manager.py
# Purpose: Track and reinforce successful fork variants across cycles
# ============================================================

import os
import json
from datetime import datetime

MEMORY_PATH = "memory_archive/fork_convergence_log.jsonl"


def score_fork_convergence(cycle, variant_id, performance_gain, confidence, regret):
    convergence_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": cycle,
        "variant_id": variant_id,
        "gain": performance_gain,
        "confidence": confidence,
        "regret": regret,
        "score": round(float(confidence) - float(regret) + float(performance_gain or 0), 4)
    }

    try:
        os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
        with open(MEMORY_PATH, "a") as f:
            f.write(json.dumps(convergence_record) + "\n")
    except Exception as e:
        print(f"[FORK CONVERGENCE ERROR] Failed to log convergence score: {e}")


if __name__ == "__main__":
    from datetime import datetime
    import os

    print("🔁 Testing fork convergence log...")
    sample_entry = {
        "cycle": 999,
        "variant_id": "TEST_FORK_ABC",
        "regret": 0.12,
        "confidence": 0.84,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        os.makedirs("memory_archive", exist_ok=True)
        with open("memory_archive/strategy_mutations.jsonl", "a") as f:
            f.write(json.dumps(sample_entry) + "\n")
        print("✅ Strategy mutation logged.")
    except Exception as e:
        print(f"❌ Strategy mutation log failed: {e}")
