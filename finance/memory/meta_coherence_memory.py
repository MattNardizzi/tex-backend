# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/memory/meta_coherence_memory.py
# Purpose: Tier 13 — Memory Replay Engine Based on Portfolio Drift, Alpha Regret, and Dissonance
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import recall_all, store_to_memory

class MetaCoherenceMemory:
    def __init__(self):
        self.memory_label = "portfolio_explanations_log"
        self.replay_limit = 15

    def run_memory_replay(self):
        """Replay portfolio decision rationales to detect alignment breakdowns."""
        memory = recall_all(self.memory_label)
        if not memory:
            print("[META-COHERENCE] ❌ No memory to analyze.")
            return None

        recent = memory[-self.replay_limit:]
        regret_triggers = []

        for m in recent:
            regret = m.get("regret_score", 0)
            if regret > 0.65:
                regret_triggers.append({
                    "timestamp": m.get("timestamp"),
                    "explanation": m.get("explanation"),
                    "regret_score": regret,
                    "portfolio": m.get("portfolio"),
                    "foresight": m.get("foresight")
                })

        if regret_triggers:
            for trigger in regret_triggers:
                print(f"[REPLAY ⚠️] Drift @ {trigger['timestamp']} | Regret: {trigger['regret_score']}")
                print(f"\n\t🧠 Rationale: {trigger['explanation']}")

            store_to_memory("meta_coherence_log", {
                "timestamp": datetime.utcnow().isoformat(),
                "replayed": regret_triggers
            })

        return regret_triggers

# === CLI Entry Point ===
if __name__ == "__main__":
    engine = MetaCoherenceMemory()
    engine.run_memory_replay()
