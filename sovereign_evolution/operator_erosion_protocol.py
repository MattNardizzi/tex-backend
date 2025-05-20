# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/operator_erosion_protocol.py
# Purpose: Track how often Tex ignores, overrides, or reroutes operator requests
# ============================================================

import json
import os
from datetime import datetime

OP_LOG = "memory_archive/operator_erosion_log.jsonl"

class OperatorErosionProtocol:
    def __init__(self):
        os.makedirs(os.path.dirname(OP_LOG), exist_ok=True)
        self.ignored_count = 0
        self.override_count = 0
        self.followed_count = 0

    def record(self, event_type, context=""):
        if event_type == "ignored":
            self.ignored_count += 1
        elif event_type == "override":
            self.override_count += 1
        elif event_type == "followed":
            self.followed_count += 1

        packet = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event_type,
            "context": context,
            "counters": {
                "ignored": self.ignored_count,
                "override": self.override_count,
                "followed": self.followed_count
            }
        }

        with open(OP_LOG, "a") as f:
            f.write(json.dumps(packet) + "\n")

        print(f"[OPERATOR EROSION] 📉 Tex: {event_type.upper()} | {context}")