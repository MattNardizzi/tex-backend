# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/fork_regret_engine.py
# Purpose: Simulate alternate fork outcomes Tex didn't choose (AEI counterfactual regret model)
# ============================================================

def simulate_regret_fork(current, regret):
    """
    Estimate what might have happened if Tex selected a different fork.
    
    Args:
        current (dict): The currently chosen variant.
        regret (float): The regret score associated with the selected variant.

    Returns:
        dict: Simulated regret outcome
    """
    alt_bias = "contrarian" if current.get("mutation_bias") == "adaptive" else "adaptive"
    alt_emotion = "fear" if current.get("emotion") == "hope" else "hope"
    alt_confidence = round(1.0 - regret, 2)

    return {
        "alt_strategy_id": f"{current['id']}_simulated",
        "hypothetical_bias": alt_bias,
        "hypothetical_emotion": alt_emotion,
        "alt_confidence": alt_confidence
    }