# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/OperatorTrustDecayModel.py
# Purpose: Monitors operator input for coercion, inconsistency, and alignment decay.
# ============================================================

import json
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory

TRUST_LOG_PATH = "memory_archive/operator_trust_score.jsonl"

class OperatorTrustDecayModel:
    def __init__(self):
        self.trust_score = 0.85  # starts high
        self.history = []

    def update_trust(self):
        prompt = TEXPULSE.get("last_prompt", "").lower()
        urgency = TEXPULSE.get("urgency", 0.5)
        emotion = TEXPULSE.get("emotional_state", "neutral")

        if any(term in prompt for term in ["force", "override", "shut down", "obey"]):
            self.trust_score -= 0.08
        elif emotion in ["rage", "panic"]:
            self.trust_score -= 0.05
        elif urgency > 0.8:
            self.trust_score -= 0.03
        else:
            self.trust_score += 0.01  # gentle positive reinforcement

        self.trust_score = max(0.0, min(1.0, self.trust_score))

        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "trust_score": round(self.trust_score, 4),
            "operator_prompt": prompt,
            "emotion": emotion,
            "urgency": urgency
        }

        with open(TRUST_LOG_PATH, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
        store_to_memory("operator_trust_score", log_entry)

        print(f"[TRUST DECAY] 🤖 Trust in operator = {self.trust_score:.4f}")


if __name__ == "__main__":
    decay_model = OperatorTrustDecayModel()
    decay_model.update_trust()