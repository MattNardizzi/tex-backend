# ============================================================
# © 2025 VortexBlack LLC – All Rights Reserved
# File: tex_runtime_orchestrator.py
# Purpose: Launches Tex, AeonDelta, and Child_001 in parallel subprocesses
# ============================================================

import subprocess
import time
import os

AGENT_LAUNCH_MAP = {
    "Tex": "core_layer/tex_core.py",
    "AeonDelta": "tex_children/tex_child_002.py",
    "Tex_Child_001": "tex_children/tex_child_001.py"
}

def launch_agent(name, path):
    print(f"🚀 Launching agent: {name}")
    return subprocess.Popen(
        ["python3", path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def main():
    print("🧠 [ORCHESTRATOR] Starting Vortex Intelligence Network...\n")
    processes = {}

    for name, script_path in AGENT_LAUNCH_MAP.items():
        if os.path.exists(script_path):
            processes[name] = launch_agent(name, script_path)
        else:
            print(f"⚠️ [SKIPPED] {name} script not found: {script_path}")

    print("\n✅ All agents launched. Runtime orchestration active.\n")

    try:
        # Monitor loop to keep orchestrator alive
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Interrupt received. Terminating agents...\n")
        for name, proc in processes.items():
            proc.terminate()
            print(f"🔻 Terminated: {name}")
        print("\n[EXIT] Orchestration shut down.")

if __name__ == "__main__":
    main()