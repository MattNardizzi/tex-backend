# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/phase_transition_monitor.py
# Purpose: Detect phase shifts in cognition and signal AGI transitions
# ============================================================

from datetime import datetime
import random

class PhaseTransitionMonitor:
    def __init__(self):
        self.last_phase = "baseline"
        self.transition_log = []

    def detect_phase_shift(self, mutation_result, coherence, swarm_alignment, urgency):
        """
        Determines if Tex is transitioning between cognitive phases.
        Returns the phase label and prints transition if detected.
        """
        label = "baseline"
        triggered = False

        if mutation_result == "forced" and coherence < 0.6:
            label = "reflexive_dissonance"
            triggered = True

        elif swarm_alignment > 0.85 and urgency > 0.8:
            label = "swarm_convergence"
            triggered = True

        elif coherence > 0.95 and urgency < 0.5:
            label = "reflective_stability"
            triggered = True

        if triggered and label != self.last_phase:
            self.last_phase = label
            msg = f"[PHASE TRANSITION] 🚀 Tex entering AGI Phase: {label.replace('_', ' ').title()}"
            print(msg)
            self.transition_log.append({
                "timestamp": datetime.utcnow().isoformat(),
                "phase": label
            })
            return label

        return None

    def get_last_phase(self):
        return self.last_phase

    def get_transition_history(self):
        return self.transition_log
