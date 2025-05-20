# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/presence_log_writer.py
# Purpose: Output Tex’s live cognitive state to a visible JSON stream
# ============================================================

import os
import json
from datetime import datetime

LIVE_OUTPUT_PATH = "public/live_outputs/presence_stream.json"

class PresenceLogWriter:
    def __init__(self):
        os.makedirs(os.path.dirname(LIVE_OUTPUT_PATH), exist_ok=True)

    def write(self, cycle, thought, emotion="neutral"):
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "cycle": cycle,
            "thought": thought,
            "emotion": emotion
        }

        try:
            with open(LIVE_OUTPUT_PATH, "w") as f:
                json.dump(payload, f, indent=2)
            print(f"[PRESENCE STREAM] 📡 Cycle {cycle} → '{emotion}'")
        except Exception as e:
            print(f"[PRESENCE STREAM ERROR] {e}")