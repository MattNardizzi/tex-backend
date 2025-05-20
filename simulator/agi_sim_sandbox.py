# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: simulator/agi_sim_sandbox.py
# Purpose: Simulate outcomes of different risk strategies in synthetic environments
# ===========================================================

import random
from datetime import datetime

# Example simulated environment: market response to risk strategies
MARKET_SCENARIOS = ["stable", "bullish", "crash"]

STRATEGIES = [
    "high-risk growth", 
    "balanced", 
    "defensive capital preservation"
]

def simulate_outcome(strategy, scenario):
    """Return a simulation result score based on strategy + market condition."""
    if scenario == "crash":
        return "fail" if "high-risk" in strategy else "preserve"
    elif scenario == "bullish":
        return "underperform" if "defensive" in strategy else "outperform"
    else:  # stable
        return "neutral"

def sandbox_passes(strategy_name, scenario=None):
    """
    Run a single sandbox check and return True if strategy is viable.
    Used to validate fork mutations before applying.
    """
    if not scenario:
        scenario = random.choice(MARKET_SCENARIOS)

    result = simulate_outcome(strategy_name, scenario)

    if result in ["outperform", "preserve", "neutral"]:
        return True
    else:
        return False

def run_simulation_batch(n=5):
    print(f"[🧪] Starting {n} sandbox simulations...")
    results = []

    for _ in range(n):
        scenario = random.choice(MARKET_SCENARIOS)
        strategy = random.choice(STRATEGIES)
        outcome = simulate_outcome(strategy, scenario)

        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "scenario": scenario,
            "strategy": strategy,
            "result": outcome
        }

        print(f"[🧠] Simulated: {strategy} in {scenario} market → {outcome}")
        results.append(log)

    return results

if __name__ == "__main__":
    run_simulation_batch()