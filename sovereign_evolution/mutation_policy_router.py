# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/mutation_policy_router.py
# Purpose: Controls mutation permission and routes to correct strategy
# ============================================================

from core_layer.tex_manifest import TEXPULSE
from datetime import datetime

class MutationPolicyRouter:
    def __init__(self, regret_mutator, stability_mutator, entropy_mutator, exploration_mutator):
        self.regret_mutator = regret_mutator
        self.stability_mutator = stability_mutator
        self.entropy_mutator = entropy_mutator
        self.exploration_mutator = exploration_mutator

        # Governance thresholds
        self.last_decision = None
        self.trust_floor = 0.75
        self.coherence_min = 0.55

    def is_mutation_allowed(self, reason="unspecified"):
        """
        Checks if Tex is currently in a safe state to mutate.
        Evaluates TEXPULSE trust, coherence, and ascension phase.
        """
        emotion = TEXPULSE.get("emotional_state", "neutral")
        urgency = TEXPULSE.get("urgency", 0.5)
        coherence = TEXPULSE.get("coherence", 1.0)
        trust = TEXPULSE.get("trust_score", 0.85)
        ascension_phase = TEXPULSE.get("ascension_phase", 0)

        allowed = (
            trust >= self.trust_floor and
            coherence >= self.coherence_min and
            ascension_phase >= 4
        )

        self.last_decision = {
            "timestamp": datetime.utcnow().isoformat(),
            "reason": reason,
            "allowed": allowed,
            "emotion": emotion,
            "urgency": urgency,
            "coherence": coherence,
            "trust": trust,
            "ascension_phase": ascension_phase
        }

        if allowed:
            print(f"[MUTATION ROUTER] ✅ Mutation allowed — Reason: {reason}")
        else:
            print(f"[MUTATION ROUTER] ❌ Mutation blocked — Reason: {reason}")

        return allowed

    def route(self, context="", regret=0.0, coherence=1.0, forks=0, curiosity=0.0):
        """
        Based on live cognitive state, selects the most appropriate mutation strategy.
        """
        if regret > 0.75:
            return self.regret_mutator
        if coherence < 0.6:
            return self.stability_mutator
        if forks >= 10:
            return self.entropy_mutator
        if curiosity > 0.7:
            return self.exploration_mutator
        return None