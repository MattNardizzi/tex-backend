# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/environmental_reflex_engine.py
# Purpose: Tier 3 AGI-Grade Adaptive Environmental Reflex Engine
# ============================================================

import uuid
import datetime
from collections import deque

class EnvironmentalReflexEngine:
    def __init__(self):
        self.event_log = deque(maxlen=100)
        self.adaptation_rules = {
            "signal_loss": "enter_recovery_mode",
            "silence": "initiate_internal_dialogue",
            "heat_spike": "coolant_override",
            "noise_anomaly": "engage_filter",
            "emotional_flatline": "trigger_reflection_loop"
        }
        self.urgency_bias_map = {
            "signal_loss": 0.8,
            "silence": 0.4,
            "heat_spike": 0.7,
            "noise_anomaly": 0.6,
            "emotional_flatline": 0.75
        }

    def inject_environmental_event(self, event_type: str, intensity: float, source: str = "system"):
        event = {
            "id": str(uuid.uuid4()),
            "timestamp": str(datetime.datetime.utcnow()),
            "event_type": event_type,
            "intensity": round(intensity, 3),
            "source": source,
            "response_triggered": None,
            "urgency_bias": self.urgency_bias_map.get(event_type, 0.5)
        }
        self.event_log.append(event)
        return event

    def evaluate_environment(self, current_emotion: str, urgency: float, coherence: float):
        responses = []
        for event in list(self.event_log):
            if not event["response_triggered"]:
                threshold = 0.6 * event["urgency_bias"]
                adjusted_intensity = event["intensity"] * (urgency + 0.5 * (1.0 - coherence))
                if adjusted_intensity >= threshold:
                    action = self.adaptation_rules.get(event["event_type"], "no_action")
                    event["response_triggered"] = action
                    response = {
                        "trigger": event["event_type"],
                        "action": action,
                        "adjusted_intensity": round(adjusted_intensity, 3),
                        "emotion": current_emotion,
                        "urgency": urgency,
                        "coherence": coherence,
                        "timestamp": event["timestamp"]
                    }
                    responses.append(response)
        return responses

    def describe_last_environmental_response(self):
        for event in reversed(self.event_log):
            if event["response_triggered"]:
                return f"Environmental event '{event['event_type']}' triggered adaptive action: {event['response_triggered']} from source: {event['source']}."
        return "No adaptive responses have been triggered yet."

    def get_environmental_log(self, limit=10):
        return list(self.event_log)[-limit:]

    def reset_environmental_log(self):
        self.event_log.clear()
