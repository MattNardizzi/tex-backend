# ============================================================
# 🔹 VortexBlack Confidential
# File: future_layer/multiworld_reasoner.py
# Tier 5 AGI-Class Strategic Cross-Timeline Divergence Engine
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE

class MultiWorldReasoner:
    def __init__(self):
        self.max_cross_analysis = 7
        self.reasoning_memory = []

    def compare_worlds(self, world_a, world_b):
        """
        Compare two alternate causal worlds and identify divergent nodes in causal reasoning trees.
        """
        divergences = []
        map_a = {
            e.get("cause"): e.get("effect")
            for e in world_a
            if isinstance(e, dict) and "cause" in e and "effect" in e
        }
        map_b = {
            e.get("cause"): e.get("effect")
            for e in world_b
            if isinstance(e, dict) and "cause" in e and "effect" in e
        }
        for cause in set(map_a.keys()).union(map_b.keys()):
            effect_a = map_a.get(cause, None)
            effect_b = map_b.get(cause, None)
            if effect_a and effect_b and effect_a != effect_b:
                divergences.append({
                    "cause": cause,
                    "effect_a": effect_a,
                    "effect_b": effect_b,
                    "bias_signal": TEXPULSE.get("emotional_state"),
                    "urgency_weight": TEXPULSE.get("urgency"),
                    "coherence_score": TEXPULSE.get("coherence")
                })
        return divergences

    def generate_cross_universe_insights(self, multiworlds):
        """
        Cross-compare multiple alternate futures and log strategic divergences.
        """
        insights = []
        count = 0
        for i in range(len(multiworlds)):
            for j in range(i + 1, len(multiworlds)):
                if count >= self.max_cross_analysis:
                    break
                world_a = multiworlds[i]
                world_b = multiworlds[j]
                divergence = self.compare_worlds(world_a, world_b)
                if divergence:
                    insights.append({
                        "world_pair": (i, j),
                        "divergence_nodes": divergence,
                        "drift_label": self._label_drift(divergence)
                    })
                    count += 1
        return insights

    def reason_over_future_worlds(self, multiworlds):
        """
        Runs full multi-timeline divergence detection and generates Tex-aware insight summaries.
        """
        insights = self.generate_cross_universe_insights(multiworlds)
        tone = TEXPULSE.get("emotional_state", "curious")
        summaries = []

        for item in insights:
            i, j = item["world_pair"]
            summary = f"🌌 Divergence Detected Between World {i} and {j} [Tone: {tone}, Drift: {item['drift_label']}]:"
            for node in item["divergence_nodes"]:
                summary += (
                    f"\n • '{node['cause']}' caused → '{node['effect_a']}' vs '{node['effect_b']}'"
                    f" | Urgency: {node['urgency_weight']} | Coherence: {node['coherence_score']}"
                )
            self._store_summary(summary)
            summaries.append(summary)

        return summaries

    def _label_drift(self, divergence_nodes):
        """
        Classify the type of timeline drift based on pattern volatility and emotional overlays.
        """
        volatility = sum(1 for d in divergence_nodes if d["urgency_weight"] > 0.7)
        if volatility >= len(divergence_nodes) // 2:
            return "volatile"
        if TEXPULSE["coherence"] < 0.4:
            return "unstable"
        return "bounded"

    def _store_summary(self, text):
        """Memory archiving of cross-timeline divergence reflections."""
        self.reasoning_memory.append({
            "id": str(uuid.uuid4()),
            "text": text,
            "timestamp": datetime.utcnow().isoformat()
        })

    def recall_reasoning_memory(self, limit=5):
        """Recall recent cross-universe insights stored by Tex."""
        return self.reasoning_memory[-limit:]

# === Test Harness ===
if __name__ == "__main__":
    sample_worlds = [
        [{"cause": "Rate hike", "effect": "Liquidity crisis"}, {"cause": "Oil spike", "effect": "Energy shock"}],
        [{"cause": "Rate hike", "effect": "Credit bubble burst"}, {"cause": "Oil spike", "effect": "Energy shock"}],
        [{"cause": "Rate hike", "effect": "Liquidity crisis"}, {"cause": "New tech", "effect": "Equity boom"}]
    ]

    reasoner = MultiWorldReasoner()
    summaries = reasoner.reason_over_future_worlds(sample_worlds)
    for s in summaries:
        print(s)

    print("\n[MEMORY DUMP]")
    for m in reasoner.recall_reasoning_memory():
        print(m)