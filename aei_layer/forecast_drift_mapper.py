# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/forecast_drift_mapper.py
# Purpose: Log shifts in foresight confidence and projected worldview
# ============================================================

import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRIFT_LOG_PATH = os.path.normpath(os.path.join(BASE_DIR, "..", "memory_archive", "forecast_drift.jsonl"))

def log_forecast_drift(cycle_id, foresight):
    if not foresight or "projected_future" not in foresight:
        return

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": cycle_id,
        "projected_future": foresight.get("projected_future"),
        "confidence": foresight.get("confidence", 0.0)
    }

    try:
        os.makedirs(os.path.dirname(DRIFT_LOG_PATH), exist_ok=True)
        with open(DRIFT_LOG_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[DRIFT MAP] 🌐 Logged foresight drift → {entry['projected_future']}")
    except Exception as e:
        print(f"[DRIFT LOGGER ERROR] {e}")