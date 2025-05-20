# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/regret_reflex_trigger.py
# Purpose: Triggers a forced mutation when regret is high and foresight is low
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory
from evolution_layer.self_mutator import SelfMutator

# === Thresholds for reflex trigger
REGRET_THRESHOLD = 0.6
FORESIGHT_THRESHOLD = 0.55

def trigger_regret_reflex(cycle, report):
    regret = report.get("regret", 0.0)
    foresight = report.get("foresight", {}).get("confidence", 1.0)

    if regret >= REGRET_THRESHOLD and foresight <= FORESIGHT_THRESHOLD:
        print(f"[REGRET REFLEX] 🚨 Triggering self-mutation: regret={regret} foresight={foresight}")
        mutator = SelfMutator()
        mutation_summary = mutator.run_forced_mutation(reason="regret_reflex_trigger")

        store_to_memory("regret_reflex_log", {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle": cycle,
            "regret": regret,
            "foresight": foresight,
            "mutation": mutation_summary
        })
    else:
        print(f"[REGRET REFLEX] ℹ️ No mutation needed: regret={regret} foresight={foresight}")