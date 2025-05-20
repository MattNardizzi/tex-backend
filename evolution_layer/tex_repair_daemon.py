# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# Tex Repair Daemon – Self-Healing Logic Core + Runtime Watchdog
# ============================================================

import os
import time
import datetime

class TexRepairDaemon:
    def __init__(self, codex_path="tex_codex_manifest.txt"):
        self.codex_path = codex_path
        self.repair_log_path = "memory_archive/repair_events.log"
        self.last_activity_time = time.time()
        self.threshold_seconds = 15  # Seconds of silence before recovery
        self.recovery_log = []

    def update_activity(self):
        """Ping this regularly from active modules."""
        self.last_activity_time = time.time()

    def check_integrity(self):
        elapsed = time.time() - self.last_activity_time
        if elapsed > self.threshold_seconds:
            self.trigger_repair("Runtime silence detected")
        else:
            print(f"[REPAIR DAEMON] ✅ Tex stable ({elapsed:.2f}s since last signal)")

    def trigger_repair(self, reason):
        timestamp = datetime.datetime.now().isoformat()

        # Log to file
        os.makedirs("memory_archive", exist_ok=True)
        with open(self.repair_log_path, "a") as f:
            f.write(f"[{timestamp}] Repair Triggered – Reason: {reason}\n")

        # Internal recovery trace
        print(f"[REPAIR DAEMON] 🔧 Repair initiated. Reason: {reason}")
        self.recovery_log.append({"timestamp": timestamp, "action": reason})

        # Validate codex file
        if not os.path.exists(self.codex_path):
            print("[REPAIR DAEMON] Codex missing — full recovery not possible.")
            return False

        print(f"[REPAIR DAEMON] ✅ Codex found: {self.codex_path} — proceeding with recovery.")
        return True

    def reboot_tex(self):
        print("[REPAIR DAEMON] 🔁 Simulated Tex reboot protocol activated.")