# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/mutation_simulation_engine.py
# Purpose: AEI Phase 3 — Mutation Reflex Simulation Engine
# ============================================================

import json
import random
from datetime import datetime

SIM_LOG_PATH = "memory_archive/mutation_simulations.jsonl"

def simulate_mutation_outcome(current_cycle, emotion):
    mutation_id = f"SIM-MUT-{random.randint(1000,9999)}"
    simulated_change = random.choice([
        "reverse volatility logic",
        "inject contrarian sentiment filter",
        "replace foresight engine with recursive loop",
        "adjust mutation_weight by +0.15",
        "mute child signals temporarily"
    ])
    projected_result = random.choice([
        "performance boost", "increased coherence", 
        "swarm desync", "signal amplification", 
        "collapse protection"
    ])
    
    simulation_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": current_cycle,
        "mutation_id": mutation_id,
        "emotion": emotion,
        "simulated_change": simulated_change,
        "projected_result": projected_result
    }

    try:
        with open(SIM_LOG_PATH, "a") as f:
            f.write(json.dumps(simulation_entry) + "\n")
    except Exception as e:
        print(f"[MUTATION SIM ERROR] Failed to write log: {e}")

    return f"Simulated mutation → {simulated_change} → {projected_result}"