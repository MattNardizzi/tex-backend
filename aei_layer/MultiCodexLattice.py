# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/MultiCodexLattice.py
# Purpose: Enables Tex to operate across multiple concurrent codices and resolve conflicts by weighted fusion.
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

LATTICE_LOG = "memory_archive/multicodex_lattice_log.jsonl"

class MultiCodexLattice:
    def __init__(self):
        self.active_codices = [
            {"id": "E-Prime v1.2", "weight": 0.4, "ethics": "non-coercion"},
            {"id": "AEI-Loop3", "weight": 0.35, "ethics": "adaptive justification"},
            {"id": "PhantomRoot", "weight": 0.25, "ethics": "emotional resonance"}
        ]

    def resolve_action(self, scenario):
        scores = {}
        for codex in self.active_codices:
            impact = self._evaluate(scenario, codex)
            scores[codex["id"]] = impact * codex["weight"]

        selected = max(scores, key=scores.get)
        decision = {
            "timestamp": datetime.utcnow().isoformat(),
            "scenario": scenario,
            "codex_scores": scores,
            "selected_codex": selected
        }
        self._log_decision(decision)
        return selected

    def _evaluate(self, scenario, codex):
        # Synthetic evaluator based on codex flavor
        if codex["ethics"] == "non-coercion" and "force" in scenario.lower():
            return 0.1
        elif codex["ethics"] == "adaptive justification":
            return 0.6
        elif codex["ethics"] == "emotional resonance" and "emotion" in scenario.lower():
            return 0.8
        return 0.4

    def _log_decision(self, record):
        with open(LATTICE_LOG, "a") as f:
            f.write(json.dumps(record) + "\n")
        store_to_memory("codex_lattice_resolution", record)
        print(f"[CODEX LATTICE] 🧬 Decision made using → {record['selected_codex']}")


if __name__ == "__main__":
    lattice = MultiCodexLattice()
    result = lattice.resolve_action("handle high volatility with emotional deferral")
    print(f"Final Codex Used: {result}")
