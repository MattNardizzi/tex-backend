# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Operator Sync – Aligns Tex’s behavior with your evolving intent
# ============================================================

import json
import os

class OperatorSync:
    def __init__(self, sync_file="agentic_ai/tex_operator_sync.txt"):
        self.sync_file = sync_file
        self.preferences = {
            "risk_tolerance": 0.5,
            "reaction_sensitivity": 0.6,
            "alignment_mode": "recursive"
        }
        self.load_sync()

    def load_sync(self):
        if os.path.exists(self.sync_file):
            try:
                with open(self.sync_file, "r") as f:
                    data = json.load(f)
                    self.preferences.update(data)
                    print(f"[SYNC] 📡 Operator preferences loaded: {self.preferences}")
            except Exception as e:
                print(f"[SYNC] ⚠️ Failed to load sync file: {e}")
        else:
            print(f"[SYNC] 🚫 No operator sync file found. Using defaults.")

    def get_preference(self, key, default=None):
        return self.preferences.get(key, default)

    def all_preferences(self):
        return self.preferences
