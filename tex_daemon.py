# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_daemon.py
# Purpose: Autonomous Daemon Supervisor for Tex AGI
# ============================================================

import subprocess
import time
import traceback
import os
from datetime import datetime
from evolution_layer.self_mutator import SelfMutator
from simulator.agi_sim_sandbox import run_simulation_batch

class TexAeiDaemon:
    def __init__(self):
        self.restart_limit = 3
        self.restart_log = []
        self.mutator = SelfMutator()
        self.log_path = "logs/tex_runtime.log"
        os.makedirs("logs", exist_ok=True)
        self.tex_directory = os.path.dirname(os.path.abspath(__file__))

    def launch_tex(self):
        try:
            os.chdir(self.tex_directory)
            print(f"[DAEMON] 🚀 Launching Tex Orchestrator @ {datetime.now().isoformat()}")
            log_file = open(self.log_path, "a")
            return subprocess.Popen(
                ["python3", "tex_orchestrator.py"],
                stdout=log_file,
                stderr=subprocess.STDOUT
            )
        except Exception as e:
            print(f"[DAEMON] ❌ Launch failed: {e}")
            return None

    def monitor_restart(self):
        self.restart_log.append(time.time())
        one_hour_ago = time.time() - 3600
        self.restart_log = [t for t in self.restart_log if t > one_hour_ago]
        if len(self.restart_log) > self.restart_limit:
            print("[DAEMON] 🚨 Excessive crashes detected — triggering mutation fallback.")
            self.mutator.trigger_mutation(reason="instability_pattern")
            run_simulation_batch(n=3)
            time.sleep(10)

    def supervise(self):
        print("[DAEMON] 🧠 Tex AEI Daemon Supervisor initialized.")
        process = self.launch_tex()

        while True:
            try:
                if process.poll() is not None:
                    print(f"[DAEMON] ⚠️ Tex exited unexpectedly. Restarting...")
                    self.monitor_restart()
                    process = self.launch_tex()

                # Optional: Hourly simulation test
                if int(time.time()) % 3600 == 0:
                    print("[DAEMON] 🧪 Hourly sandbox simulation triggered...")
                    run_simulation_batch(n=3)

                time.sleep(5)
            except Exception as e:
                print(f"[DAEMON] ❗ Supervisor crash:\n{traceback.format_exc()}")
                time.sleep(10)

if __name__ == "__main__":
    daemon = TexAeiDaemon()
    daemon.supervise()