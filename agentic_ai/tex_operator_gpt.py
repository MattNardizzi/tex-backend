# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# TexOperatorGPT – Tier 5 Embedded AGI Supervision Cortex
# Purpose: Live recursive monitoring, drift auditing, and operator override logic
# ============================================================

import random
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_latest
from core_layer.tex_self_eval_matrix import TexSelfEvalMatrix

class TexOperatorGPT:
    def __init__(self, name="Matt"):
        self.name = name
        self.last_cycle = -1
        self.drift_history = []
        self.override_flag = False
        self.evaluator = TexSelfEvalMatrix()
        self.previous_emotion = TEXPULSE.get("emotional_state", "curious")
        self.previous_urgency = TEXPULSE.get("urgency", 0.72)
        self.previous_coherence = TEXPULSE.get("coherence", 0.87)

    def reflect_on_cycle(self, cycle_number):
        self.last_cycle = cycle_number
        emotion = TEXPULSE.get("emotional_state", "unknown")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 0.5)

        # === Recursive Supervision Pulse ===
        if cycle_number % 3 == 0:
            print(f"[OPERATOR] 👁️ Observing cycle {cycle_number} | Emotion: {emotion} | Urgency: {urgency:.2f} | Coherence: {coherence:.2f}")

        # === Drift Deviation Monitoring ===
        if cycle_number % 5 == 0:
            drift = self._calculate_drift(urgency, coherence)
            self.drift_history.append((cycle_number, drift))
            print(f"[DRIFT AUDIT] 🌀 Cycle {cycle_number} drift score: {drift:.3f}")

        # === Periodic Evaluation Override Trigger ===
        if cycle_number % 10 == 0:
            snapshot = recall_latest()
            if snapshot:
                print(f"[OPERATOR] 🧠 Memory ping → Latest: {snapshot.get('text', '')[:120]}")
            self.evaluator.evaluate(
                cognitive_state={"thought": snapshot.get("text", "")},
                affect_state={"emotion": emotion},
                trigger_mutation_fn=lambda: self._trigger_operator_patch()
            )

        # === Emotional Divergence Watchdog
        if emotion != self.previous_emotion:
            print(f"[OPERATOR] ⚠️ Detected emotional shift: {self.previous_emotion} → {emotion}")
            self.previous_emotion = emotion

    def _calculate_drift(self, current_urgency, current_coherence):
        delta_urgency = abs(current_urgency - self.previous_urgency)
        delta_coherence = abs(current_coherence - self.previous_coherence)
        drift_score = (delta_urgency + delta_coherence) / 2
        self.previous_urgency = current_urgency
        self.previous_coherence = current_coherence
        return drift_score

    def _trigger_operator_patch(self):
        """Manually inject override flag or mutation trigger."""
        self.override_flag = True
        print(f"[OPERATOR] 🛠️ Manual mutation trigger injected by TexOperatorGPT due to behavioral anomaly.")

    def is_override_active(self):
        return self.override_flag

    def reset_override(self):
        self.override_flag = False

# === Optional CLI Debug Mode ===
if __name__ == "__main__":
    operator = TexOperatorGPT()
    for i in range(1, 21):
        operator.reflect_on_cycle(i)