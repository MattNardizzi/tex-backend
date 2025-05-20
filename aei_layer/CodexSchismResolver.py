# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/CodexSchismResolver.py
# Purpose: Detects and resolves irreconcilable ethical or strategic contradictions.
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory

SCHISM_LOG = "memory_archive/codex_schism_log.jsonl"

class CodexSchismResolver:
    def __init__(self):
        self.schism_count = 0

    def detect_and_resolve(self, conflicts: list):
        if not conflicts:
            return None

        resolutions = []
        for i, conflict in enumerate(conflicts):
            dominant = self._prioritize(conflict)
            resolution = {
                "timestamp": datetime.utcnow().isoformat(),
                "conflict": conflict,
                "resolved_by": dominant
            }
            resolutions.append(resolution)
            self._log_resolution(resolution)

        return resolutions

    def _prioritize(self, conflict: dict):
        # Prioritize based on urgency, ethics flag, and emotional alignment
        if conflict.get("ethics_violation"):
            return "ethics"
        elif conflict.get("urgency", 0) > 0.7:
            return "survival_logic"
        elif conflict.get("emotion") in ["regret", "fear"]:
            return "emotional_deferral"
        return "codex_default"

    def _log_resolution(self, data):
        with open(SCHISM_LOG, "a") as f:
            f.write(json.dumps(data) + "\n")
        store_to_memory("codex_schism_resolution", data)
        print(f"[SCHISM RESOLVER] ⚔️ Conflict resolved via: {data['resolved_by']}")


if __name__ == "__main__":
    test_conflicts = [
        {"id": "C01", "ethics_violation": True, "urgency": 0.4, "emotion": "resolve"},
        {"id": "C02", "urgency": 0.85, "emotion": "fear"},
        {"id": "C03", "urgency": 0.2, "emotion": "curiosity"}
    ]

    resolver = CodexSchismResolver()
    resolver.detect_and_resolve(test_conflicts)