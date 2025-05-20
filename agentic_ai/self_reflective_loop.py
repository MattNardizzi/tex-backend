# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Self-Reflective Loop — Meta-Cognition Layer (Upgraded)
# ============================================================

from datetime import datetime

class SelfReflectiveLoop:
    def __init__(self):
        self.history = []

    def assess(self, cycle_number: int):
        now = datetime.utcnow()
        self.history.append((cycle_number, now))

        if len(self.history) > 5:
            drift = self.history[-1][0] - self.history[-6][0]
            time_drift = (self.history[-1][1] - self.history[-6][1]).total_seconds()
            if drift < 5 or time_drift < 12:
                print(f"[REFLECTOR] ⚠️ Loop redundancy risk — Drift: {drift} | Time Drift: {time_drift:.2f}s")
            else:
                print("[REFLECTOR] ✅ Temporal-cognitive rhythm stable.")
        else:
            print("[REFLECTOR] 🧠 Meta-memory calibrating...")