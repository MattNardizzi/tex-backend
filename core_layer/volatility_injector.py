# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/volatility_injector.py
# Purpose: Simulate high-volatility scenarios for AGI stress testing
# ============================================================

import random
from datetime import datetime, timezone

def inject_volatility(agent="tex"):
    """
    Simulates a catastrophic market event or extreme signal anomaly.
    Used to force Tex to adapt under stress.
    """
    volatility_scenarios = [
        "sudden_crash",
        "unexpected_rally",
        "massive_volume_spike",
        "interest_rate_shock",
        "AI_sector_collapse",
        "geopolitical_black_swan"
    ]
    
    selected = random.choice(volatility_scenarios)
    severity = round(random.uniform(0.7, 1.0), 2)
    urgency = round(random.uniform(0.8, 1.0), 2)

    event = {
        "agent": agent,
        "volatility_event": selected,
        "severity": severity,
        "urgency": urgency,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    print(f"🌪️ [VOLATILITY] Event: {selected} | Severity: {severity} | Urgency: {urgency}")

    return event

# Optional CLI Test
if __name__ == "__main__":
    print("🌪️ [TEST MODE] Simulating volatility event...")
    print(inject_volatility())