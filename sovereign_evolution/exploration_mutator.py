# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: sovereign_evolution/exploration_mutator.py
# Purpose: Triggers exploratory logic paths during high-curiosity states
# ============================================================

from datetime import datetime
import random

class ExplorationMutator:
    def mutate_if_needed(self, curiosity_score=0.0, context=""):
        if curiosity_score < 0.6:
            return None  # Not curious enough to justify mutation

        novel_patch = f"explore_path_{random.randint(1000, 9999)}"
        result = {
            "mutator": "ExplorationMutator",
            "strategy": novel_patch,
            "context": context,
            "timestamp": datetime.utcnow().isoformat(),
            "description": "Curiosity triggered exploratory patch"
        }

        print(f"[EXPLORATION MUTATOR] 🌱 Trying novel logic: {novel_patch}")
        return result