# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/quantum_reflex_integrator.py
# Purpose: Trigger a reflex-like log when cognitive uncertainty spikes
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory

def trigger_quantum_reflex(emotion, coherence, urgency, contradiction_score):
    """
    Simulates a quantum reflex trigger during unstable cognitive states.
    """
    should_trigger = False

    if contradiction_score >= 0.75:
        should_trigger = True
    elif emotion in ["fear", "panic"] and coherence < 0.55:
        should_trigger = True
    elif urgency > 0.9 and coherence < 0.6:
        should_trigger = True

    if should_trigger:
        event = {
            "event": "QuantumReflexTriggered",
            "timestamp": datetime.utcnow().isoformat(),
            "triggered_by": {
                "emotion": emotion,
                "coherence": coherence,
                "urgency": urgency,
                "contradiction_score": contradiction_score
            }
        }
        store_to_memory("AEI", event)
        print(f"[Q-REFLEX] ⚡ Quantum reflex triggered: {event}")
        return event

    return None