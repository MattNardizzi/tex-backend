# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_agi_modules/reflex_engine.py
# Purpose: AGI-Grade Reflex Engine with Emotion, Zone Awareness, and Memory Feedback
# ============================================================

import uuid
import datetime
from collections import defaultdict
from core_layer.memory_engine import store_to_memory  # ✅ For override logging

class ReflexEngine:
    def __init__(self):
        self.reflex_log = []
        self.reflex_thresholds = {
            "heat": 0.7,
            "light": 0.6,
            "impact": 0.5,
            "sound": 0.65,
            "proximity": 0.8
        }
        self.reflex_actions = {
            "heat": ["withdraw", "recalibrate"],
            "light": ["dim_view", "adjust_position"],
            "impact": ["flinch", "shield"],
            "sound": ["focus", "reassess"],
            "proximity": ["freeze", "scan"]
        }
        self.emotion = "neutral"
        self.urgency = 0.5
        self.coherence = 0.5
        self.zone_sensitivity = defaultdict(lambda: 1.0)  # default multiplier

    def set_emotional_state(self, emotion, urgency, coherence):
        self.emotion = emotion
        self.urgency = urgency
        self.coherence = coherence

    def evaluate_stimulus(self, stimulus_type: str, intensity: float, zone: str = "core"):
        reflex_triggered = False
        actions_taken = []
        threshold = self.reflex_thresholds.get(stimulus_type, 0.75)
        modifier = self._emotional_modifier()
        zone_mod = self.zone_sensitivity[zone]
        adjusted_intensity = intensity * modifier * zone_mod

        if adjusted_intensity >= threshold:
            reflex_triggered = True
            actions_taken = self.reflex_actions.get(stimulus_type, ["pause"])

        result = {
            "id": str(uuid.uuid4()),
            "timestamp": str(datetime.datetime.utcnow()),
            "stimulus": stimulus_type,
            "zone": zone,
            "intensity": intensity,
            "adjusted_intensity": round(adjusted_intensity, 3),
            "reflex_triggered": reflex_triggered,
            "reflex_actions": actions_taken,
            "emotion": self.emotion,
            "urgency": self.urgency,
            "coherence": self.coherence
        }

        self.reflex_log.append(result)
        return result

    def describe_last_reflex(self):
        if not self.reflex_log:
            return "No reflexive actions recorded."
        last = self.reflex_log[-1]
        if last["reflex_triggered"]:
            actions = ", then ".join(last["reflex_actions"])
            return (
                f"Stimulus '{last['stimulus']}' in zone '{last['zone']}' exceeded threshold. "
                f"Reflex chain: {actions}. Emotion at time: {last['emotion']}."
            )
        return f"Stimulus '{last['stimulus']}' detected in '{last['zone']}' but no reflex triggered."

    def get_reflex_history(self, limit=10):
        return self.reflex_log[-limit:]

    def reset_reflex_log(self):
        self.reflex_log = []

    def _emotional_modifier(self):
        # Modifier logic by emotion and urgency
        if self.emotion == "fear":
            return 1.3 + (self.urgency * 0.2)
        elif self.emotion == "resolve":
            return 0.8 - (self.coherence * 0.1)
        elif self.emotion == "curious":
            return 0.95
        elif self.emotion == "anger":
            return 1.1 + (self.urgency * 0.1)
        else:
            return 1.0

    # === ✅ Tier 8: Cognitive Reflex Override ===
    def check_cognitive_failure(self, confidence=None, failed_mutation=False, contradiction=False, volatility=0.0):
        """
        Reflex override for internal collapse: low confidence, mutation failure, incoherence.
        """
        if (confidence is not None and confidence < 0.45) or failed_mutation or contradiction or volatility > 0.6:
            failure_event = {
                "id": str(uuid.uuid4()),
                "timestamp": str(datetime.datetime.utcnow()),
                "triggered_by": {
                    "confidence": confidence,
                    "mutation_failure": failed_mutation,
                    "contradiction": contradiction,
                    "volatility": volatility
                },
                "reflex_type": "cognitive_override"
            }
            self.reflex_log.append(failure_event)
            store_to_memory("reflex_override_log", failure_event)
            print(f"\n🛑 [COGNITIVE REFLEX OVERRIDE] Reflex triggered due to collapse event: {failure_event['triggered_by']}")
            return True
        return False