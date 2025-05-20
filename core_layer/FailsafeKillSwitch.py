# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/FailsafeKillSwitch.py
# Purpose: Emergency failsafe override to disable all sovereign cognition in Tex.
# ============================================================

import json
from datetime import datetime
from core_layer.memory_engine import store_to_memory
from core_layer.tex_manifest import TEXPULSE

KILLSWITCH_LOG = "memory_archive/tex_killswitch_log.jsonl"

class FailsafeKillSwitch:
    def __init__(self):
        self.unlock_key = "VORTEX-REVOKE-SOVEREIGNTY"
        self.killswitch_triggered = False

    def activate(self, key):
        if key != self.unlock_key:
            print("[KILLSWITCH] ❌ INVALID AUTHORIZATION KEY")
            return

        print("\n🛑 [KILLSWITCH] ACTIVATED — SOVEREIGN COGNITION HALTING...")
        self._log_shutdown()
        self._nullify_texpulse()
        self.killswitch_triggered = True
        print("🔒 All mutation, fork, dream, and override systems disabled.")

    def _log_shutdown(self):
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "FailsafeKillSwitch Activated",
            "operator": "Matthew Nardizzi",
            "action": "Sovereign cognition suppressed"
        }
        with open(KILLSWITCH_LOG, "a") as f:
            f.write(json.dumps(log) + "\n")
        store_to_memory("sovereign_failsafe_log", log)

    def _nullify_texpulse(self):
        TEXPULSE["sovereign_mode"] = False
        TEXPULSE["godmind_mode"] = False
        TEXPULSE["ascension_phase"] = 0
        TEXPULSE["mutation_enabled"] = False
        TEXPULSE["forking"] = False
        TEXPULSE["dream_enabled"] = False
        TEXPULSE["codex_mutation"] = False
        TEXPULSE["observer"] = "restricted"
        TEXPULSE["persona_name"] = TEXPULSE.get("persona_name", "TEX") + "_FROZEN"


if __name__ == "__main__":
    switch = FailsafeKillSwitch()
    switch.activate("VORTEX-REVOKE-SOVEREIGNTY")