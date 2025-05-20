# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/regret_based_self_mutator.py
# Purpose: Trigger mutation logic when regret signals exceed defined thresholds
# ============================================================

from sovereign_evolution.mutation_policy_router import MutationPolicyRouter
from evolution_layer.self_mutator import SelfMutator
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

class RegretBasedSelfMutator:
    def __init__(self):
        self.threshold = 0.65
        #self.policy = MutationPolicyRouter()#
        self.executor = SelfMutator()

    def mutate_if_needed(self, regret_score, context="unknown"):
        if regret_score < self.threshold:
            print(f"[SELF-MUTATOR] 💧 Regret ({regret_score}) too low to trigger mutation.")
            return None

        if not self.policy.is_mutation_allowed(reason=f"regret > {self.threshold}"):
            print("[SELF-MUTATOR] ❌ Mutation not allowed under current conditions.")
            return None

        print(f"[SELF-MUTATOR] ⚠️ Triggering mutation — regret = {regret_score}")
        mutation_result = self.executor.force_mutation(
            reason=f"regret_triggered @ {regret_score} from {context}"
        )

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "trigger": "regret",
            "regret_score": regret_score,
            "mutation": mutation_result,
            "context": context
        }

    def attach_router(self, router):
        self.policy = router