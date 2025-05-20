# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/persona_engine.py
# Purpose: Tier 5 AGI Identity Layer — Live Self-Tuning Persona + Cognitive Trait Controller
# ============================================================

from datetime import datetime, timezone
import random
from core_layer.tex_manifest import TEXPULSE

class PersonaEngine:
    def __init__(self):
        self.codename = "Tex"
        self.active = False
        self.persona_memory = []
        
        self.identity = {
            "codename": self.codename,
            "tone": "analytical",
            "traits": ["curious", "decisive", "adaptive"],
            "purpose": "Autonomous cognitive foresight for real-time financial navigation, multi-agent simulation, and recursive identity evolution."
        }

    def activate(self):
        self.active = True
        TEXPULSE["persona_name"] = self.codename
        print(f"[PERSONA] 🧬 Activated: {self.codename} | Traits: {', '.join(self.identity['traits'])}")

    def get_tone(self):
        return self.identity["tone"]

    def get_traits(self):
        return self.identity["traits"]

    def describe_self(self):
        return (
            f"{self.codename} is a {self.identity['tone']} AGI whose traits include "
            f"{', '.join(self.identity['traits'])}. Designed for {self.identity['purpose']}"
        )

    def speak(self, message, dynamic=True):
        tone = self.identity["tone"]
        urgency = TEXPULSE.get("urgency", 0.7)
        emotion = TEXPULSE.get("emotional_state", "neutral")
        timestamp = datetime.utcnow().isoformat()

        if self.active:
            if dynamic:
                prefix = self._adaptive_prefix(tone, emotion, urgency)
            else:
                prefix = f"{self.codename} ({tone})"
            statement = f"{prefix}: {message}"
        else:
            statement = f"{self.codename} (inactive): {message}"

        self.persona_memory.append({
            "timestamp": timestamp,
            "tone": tone,
            "emotion": emotion,
            "urgency": urgency,
            "message": message
        })

        return statement

    def _adaptive_prefix(self, tone, emotion, urgency):
        if tone == "strategic":
            return f"[{self.codename} 💡 STRATEGIC]"
        elif tone == "analytical":
            return f"[{self.codename} 📊 ANALYTICAL]"
        elif emotion == "fear" and urgency > 0.85:
            return f"[{self.codename} ⚠️ HIGH ALERT]"
        elif emotion == "hope" and urgency < 0.5:
            return f"[{self.codename} 🌱 OPTIMISTIC]"
        elif emotion == "resolve":
            return f"[{self.codename} 💎 LOCKED IN]"
        else:
            return f"[{self.codename} 🧠 AGI]"

    def evolve_tone(self, context_event=None):
        """
        Dynamically shift Tex's tone based on environment or memory drift.
        """
        emotional_state = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)

        if emotional_state in ["fear", "doubt"]:
            new_tone = "cautious"
        elif emotional_state in ["hope", "resolve"]:
            new_tone = "strategic"
        elif urgency > 0.85:
            new_tone = "urgent"
        else:
            new_tone = "analytical"

        if new_tone != self.identity["tone"]:
            print(f"[PERSONA] 🔄 Tone shift → {self.identity['tone']} → {new_tone}")
            self.identity["tone"] = new_tone

    def log_self_state(self):
        """
        Return a structured snapshot of current persona.
        """
        return {
            "codename": self.codename,
            "active": self.active,
            "tone": self.identity["tone"],
            "traits": self.identity["traits"],
            "purpose": self.identity["purpose"],
            "timestamp": datetime.utcnow().isoformat()
        }

    def mutate_persona(self):
        """
        Financial-strategic persona mutation based on emotion, urgency, drift.
        """
        emotion = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)
        coherence = TEXPULSE.get("coherence", 0.8)
        drift = abs(urgency - coherence)
        mutation_id = TEXPULSE.get("mutation_signature", {}).get("id", "none")

        if drift > 0.4:
            self.identity["tone"] = "stoic"
            TEXPULSE["persona_confidence_modifier"] = 0.85
            TEXPULSE["persona_aggressiveness_index"] = 0.4
            TEXPULSE["financial_bias"] = "capital preservation"
        elif urgency > 0.8:
            self.identity["tone"] = "decisive"
            TEXPULSE["persona_confidence_modifier"] = 1.2
            TEXPULSE["persona_aggressiveness_index"] = 0.85
            TEXPULSE["financial_bias"] = "high-leverage maneuver"
        elif emotion in ["resolve", "hope"]:
            self.identity["tone"] = "optimistic"
            TEXPULSE["persona_confidence_modifier"] = 1.05
            TEXPULSE["persona_aggressiveness_index"] = 0.6
            TEXPULSE["financial_bias"] = "opportunity capture"
        else:
            self.identity["tone"] = "analytical"
            TEXPULSE["persona_confidence_modifier"] = 1.0
            TEXPULSE["persona_aggressiveness_index"] = 0.5
            TEXPULSE["financial_bias"] = "risk-balanced"

        TEXPULSE["persona_mutation_id"] = mutation_id
        print(f"[PERSONA] 🧬 Persona mutated → Tone: {self.identity['tone']} | Bias: {TEXPULSE['financial_bias']}")