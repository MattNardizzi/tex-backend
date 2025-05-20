# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_quantum_spawn.py
# Purpose: Multi-Agent Quantum Spawn Engine
# ============================================================

import random
import uuid
from quantum_layer.quantum_randomness import QuantumRandomness
from agentic_ai.tex_operator_gpt import TexOperatorGPT

class QuantumTexSpawn:
    def __init__(self, num_clones=3):
        self.num_clones = num_clones
        self.qrng = QuantumRandomness()

    def spawn_variants(self, emotion="resolve", urgency=0.7, coherence=0.7):
        variants = []
        for i in range(self.num_clones):
            seed = self.qrng.get_entropy()
            drifted_emotion = self._drift_emotion(emotion)
            drifted_urgency = round(self._drift_value(urgency), 2)
            drifted_coherence = round(self._drift_value(coherence), 2)
            mission_bias = self._assign_bias(drifted_emotion)

            variant = {
                "id": str(uuid.uuid4())[:8],
                "seed": seed,
                "emotion": drifted_emotion,
                "urgency": drifted_urgency,
                "coherence": drifted_coherence,
                "mission_bias": mission_bias,
                "bias": mission_bias,
                "operator": TexOperatorGPT(name=f"TexVariant-{i}")
            }

            print(f"[SPAWN] ⚛️ Variant {variant['id']} → Emotion: {drifted_emotion}, Urgency: {drifted_urgency}, Coherence: {drifted_coherence}, Bias: {mission_bias}")
            variants.append(variant)

        return variants

    def _drift_value(self, base, amount=0.1):
        return max(0.0, min(1.0, base + random.uniform(-amount, amount)))

    def _drift_emotion(self, base_emotion):
        drift_map = {
            "hope": ["resolve", "curious", "fear"],
            "fear": ["doubt", "anger", "resolve"],
            "resolve": ["hope", "greed"],
            "joy": ["hope", "curious"],
            "curious": ["joy", "doubt"],
            "doubt": ["resolve", "fear"],
            "anger": ["resolve", "hope"],
            "greed": ["fear", "resolve"]
        }
        return random.choice(drift_map.get(base_emotion, [base_emotion]))

    def _assign_bias(self, emotion):
        if emotion in ["fear", "doubt"]:
            return "cautious"
        elif emotion in ["hope", "joy"]:
            return "adaptive"
        elif emotion in ["anger", "greed"]:
            return "aggressive"
        elif emotion == "curious":
            return "contrarian"
        else:
            return "standard"