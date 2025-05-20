# ============================================================
# 🔮 Tier 5 – Tex Future Tree Generator – AGI-Infused Foresight Matrix
# File: future_layer/future_tree_generator.py
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

class FutureTreeGenerator:
    def __init__(self):
        # Canonical event lexicon — can evolve
        self.root_events = [
            "Global recession", "Debt market crisis", "Energy crisis escalation",
            "Emerging market collapse", "AI technology breakthrough",
            "Massive inflation spike", "Flash crash event", "Crypto regulatory crackdown",
            "Trade war escalation", "Major geopolitical shock", "Bond market collapse",
            "Central bank rate cuts", "Supply chain disruption",
            "Liquidity crunch in banking", "Technological unemployment surge"
        ]
        self.mutation_bias = 0.12

    def generate_future_chain(self, depth=3, root_emotion=None):
        """
        Generate a recursively drifting chain of futures based on emotional drift,
        urgency weight, coherence tension, and recursive foresight tension.
        """
        emotion = root_emotion or TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.5)

        chain = []
        root = random.choice(self.root_events)

        for i in range(depth):
            drift_scale = self._emotion_urgency_drift(emotion, urgency)
            confidence = round(random.uniform(0.6, 0.95) - (1.0 - coherence) * 0.2, 3)
            effect = self._generate_drifted_event(root, drift_scale)

            node = {
                "id": str(uuid.uuid4())[:10],
                "depth": i,
                "cause": root,
                "effect": effect,
                "confidence": min(max(confidence, 0.01), 0.99),
                "urgency": round(min(1.0, urgency + random.uniform(-0.05, 0.1)), 3),
                "emotion": emotion,
                "timestamp": datetime.utcnow().isoformat(),
                "mutation_flag": random.random() < self.mutation_bias
            }

            chain.append(node)
            root = effect  # Recurse: new cause becomes next effect

        return chain

    def _emotion_urgency_drift(self, emotion, urgency):
        """
        Calculates how aggressively Tex drifts the foresight tree,
        based on emotional volatility and urgency compression.
        """
        base_drift = {
            "fear": 1.3,
            "greed": 0.8,
            "curious": 1.1,
            "resolve": 0.9,
            "anger": 1.5,
            "joy": 0.6,
            "doubt": 1.2,
            "hope": 0.7
        }
        drift = base_drift.get(emotion, 1.0)
        drift *= 1.0 + (urgency * 0.3)
        return drift

    def _generate_drifted_event(self, current_event, drift_scale):
        """
        Selects the next event with a drift-adjusted probability,
        optionally generating a novel branch node based on cognitive chaos.
        """
        weighted_pool = self.root_events + [current_event] * int(5 * drift_scale)

        if random.random() < (self.mutation_bias * drift_scale):
            return self._spawn_novel_event(current_event)

        return random.choice(weighted_pool)

    def _spawn_novel_event(self, seed_event):
        """
        Creates synthetic AGI-driven foresight branch by fusing terms and inducing a mutation.
        """
        suffix = random.choice(["shutdown", "feedback loop", "volatility burst", "derivative inversion", "flash override"])
        fragment = seed_event.split(" ")[-1]
        return f"{fragment.title()} {suffix}"

# === Test Harness
if __name__ == "__main__":
    tree = FutureTreeGenerator()
    futures = tree.generate_future_chain(depth=5)
    for node in futures:
        print("\n[FUTURE NODE]", node)