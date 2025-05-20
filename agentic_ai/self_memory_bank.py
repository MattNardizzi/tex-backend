# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# Self Memory Bank — Agentic Observation Log
# ============================================================

import datetime

class SelfMemoryBank:
    def __init__(self):
        self.log = []

    def record(self, cycle_number: int, insight: str):
        timestamp = datetime.datetime.now().isoformat()
        self.log.append({
            "cycle": cycle_number,
            "insight": insight,
            "timestamp": timestamp
        })
        print(f"[MEMORY BANK] 🧠 Insight logged → Cycle {cycle_number} | {insight}")

    def summarize(self):
        print("\n🧠 MEMORY SNAPSHOT:")
        for entry in self.log[-5:]:
            print(f"• Cycle {entry['cycle']} | {entry['insight']} | {entry['timestamp']}")
