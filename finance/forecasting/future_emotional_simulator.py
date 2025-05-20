# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: future_layer/future_emotion_simulator.py
# Purpose: Full Cognitive-Emotional Future Simulation Engine for Tex AGI
# ============================================================

import random
import uuid
from datetime import datetime

from core_layer.tex_manifest import TEXPULSE

class FutureEmotionalSimulator:
    def __init__(self):
        self.mutation_threshold = 0.85  # Trigger mutation if emotional stress > 0.85
        self.max_branches = 3

    def simulate_emotional_reactions(self):
        """Generates future projections influenced by emotion, urgency, coherence, mutation."""
        futures = []

        for _ in range(self.max_branches):
            future_id = str(uuid.uuid4())
            base_emotion = random.choice(["hope", "fear", "resolve", "doubt", "greed"])
            urgency = round(random.uniform(0.4, 1.0), 2)
            coherence = round(random.uniform(0.5, 1.0), 2)
            mutation_triggered = False
            swarm_projection = random.choice(["agreement", "divergence", "contradiction"])
            memory_drift_factor = round(random.uniform(0.0, 0.5), 2)
            confidence = coherence * (1 - memory_drift_factor)

            # Mutation Reflex
            if urgency > self.mutation_threshold or random.random() < 0.2:
                mutation_triggered = True
                base_emotion = random.choice(["resolve", "aggression", "desperation"])
                confidence *= 1.1

            futures.append({
                "future_id": future_id,
                "predicted_emotion": base_emotion,
                "urgency": urgency,
                "coherence": coherence,
                "mutation_triggered": mutation_triggered,
                "swarm_projection": swarm_projection,
                "memory_drift_factor": memory_drift_factor,
                "confidence": round(min(confidence, 1.0), 2),
                "generated_at": datetime.utcnow().isoformat()
            })

        return futures

    def summarize_emotional_paths(self, futures):
        """Summarizes emotional and strategic dynamics of projected futures."""
        summaries = []
        for f in futures:
            mutation_note = "(Mutation occurred)" if f["mutation_triggered"] else "(No mutation)"
            summaries.append(
                f"If emotion '{f['predicted_emotion']}' with urgency {f['urgency']} and coherence {f['coherence']}, "
                f"then {f['swarm_projection']} likely. {mutation_note} | Confidence: {f['confidence']}"
            )
        return summaries


# === Usage Example ===
if __name__ == "__main__":
    simulator = FutureEmotionSimulator()
    futures = simulator.simulate_emotional_reactions()
    summaries = simulator.summarize_emotional_paths(futures)
    for s in summaries:
        print("[FUTURE SIM]", s)