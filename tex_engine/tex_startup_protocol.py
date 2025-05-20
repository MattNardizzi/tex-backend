# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_engine/tex_startup_protocol.py
# Purpose: Launch Protocol for Tex — AEI Core Boot Analysis
# ============================================================

from tex_engine.boot_state_loader import load_prior_state

def run_startup_protocol():
    print("[STARTUP] 🚀 Initializing Tex boot protocol...")
    state = load_prior_state()

    print(f"[STARTUP] 🧠 Restored {len(state['memory_log'])} memories")
    print(f"[STARTUP] 🎯 Goals loaded: {len(state['goal_log'])}")
    print(f"[STARTUP] 🔬 Mutations: {len(state['mutation_log'])}")
    print(f"[STARTUP] 🧬 Variants: {len(state['variant_log'])}")
    print(f"[STARTUP] 🌍 Last cycle: {state['last_cycle']}")

    # Optional health check
    if state["last_cycle"] > 10000:
        print("[STARTUP] ⚠️ High cycle count — Consider archiving memory soon.")

    return state

if __name__ == "__main__":
    run_startup_protocol()