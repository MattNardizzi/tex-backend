# ============================================================
# © 2025 VortexBlack LLC – Tex Variant Swarm Specializer
# File: tex_children/variant_specializer.py
# Purpose: Assign financial roles and biases to spawned variants
# ============================================================

import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

class VariantSpecializer:
    def __init__(self):
        self.roles = ["risk_sentinel", "momentum_chaser", "volatility_mapper", "macro_hedger", "liquidity_sniper"]

    def assign_specialization(self, variant_id, emotion, bias):
        """
        Assigns a specialized financial cognition role to a new variant based on emotion and bias.
        """
        role = random.choice(self.roles)
        profile = {
            "variant_id": variant_id,
            "role": role,
            "emotion": emotion,
            "bias": bias,
            "timestamp": datetime.utcnow().isoformat()
        }

        store_to_memory("variant_specializations", profile)
        print(f"[VARIANT ROLE] 🧬 {variant_id} → {role} | Bias: {bias} | Emotion: {emotion}")
        return role