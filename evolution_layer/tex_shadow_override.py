# ============================================================
# 🔪 Tex Shadow Override Engine — Cognitive Fork Executor
# Purpose: Run shadow agents in parallel and selectively override live decisions
# License: © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import uuid
import time
from evolution_layer.tex_shadowlab import TexShadowLab

class TexShadowOverride:
    def __init__(self):
        self.lab = TexShadowLab()
        self.active_overrides = []
        self.override_threshold = 0.82  # Minimum score to override live logic

    def run_override_check(self, mutation_patch, live_decision, context):
        print("\n[SHADOW OVERRIDE] Launching forked cognition test...")
        shadow_agents = []

        # === Fork 3 cognitive shadows with emotional variations ===
        for _ in range(3):
            agent = self.lab.spawn_shadow_agent(
                mutation_code=mutation_patch,
                emotion_bias=random.choice(["hope", "resolve", "fear"])
            )
            agent = self.lab.simulate_outcome(agent)
            shadow_agents.append(agent)

        # === Evaluate best agent ===
        best = max(shadow_agents, key=lambda a: a["score"])
        print(f"[SHADOW OVERRIDE] Top agent: {best['id']} | Score: {best['score']} | Bias: {best['emotion_bias']}")

        if best["score"] >= self.override_threshold:
            decision_packet = {
                "override": True,
                "reason": f"Shadow agent {best['id']} outperformed baseline.",
                "score": best["score"],
                "shadow_bias": best["emotion_bias"],
                "replacement_decision": f"[FORGED] Adjusted logic with {best['emotion_bias']} temperament."
            }
            self.active_overrides.append(decision_packet)
            print("[SHADOW OVERRIDE] ✅ Override approved. Live decision replaced.")
            return decision_packet

        print("[SHADOW OVERRIDE] ❌ Override rejected. Live decision remains.")
        return {
            "override": False,
            "score": best["score"],
            "reason": "No shadow agents exceeded override threshold."
        }

    def get_override_log(self, limit=5):
        return self.active_overrides[-limit:]