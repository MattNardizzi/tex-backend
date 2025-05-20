# ============================================================
# 🧠 Vortex Operator — Embedded Cognitive Strategist for Tex
# Purpose: Internal reasoning synthesizer & mutation advisor
# Owner: Tex Core System (Matthew Nardizzi / VortexBlack LLC)
# ============================================================

from datetime import datetime
from core_layer.memory_engine import store_to_memory

class VortexOperator:
    def __init__(self):
        self.name = "Vortex"
        self.role = "Strategic Cognitive Interface"
        self.active = True
        self.last_summary = ""

    def evaluate_state(self, internal_state: dict) -> str:
        """
        Analyze Tex's internal emotional, coherence, urgency, and mutation state
        to generate a strategic explanation for use in tex_explains.
        """
        emotion = internal_state.get("emotion", "unknown")
        urgency = internal_state.get("urgency", 0.0)
        coherence = internal_state.get("coherence", 0.0)
        mutation_risk = internal_state.get("mutation_risk", 0.0)
        dominant_agent = internal_state.get("dominant_agent", "unknown")
        cycle = internal_state.get("cycle", "N/A")

        summary = f"""
        [Cycle {cycle}] Vortex Operational Report
        • Emotion: {emotion}
        • Urgency: {urgency:.2f}
        • Coherence: {coherence:.2f}
        • Mutation Risk: {mutation_risk:.2f}
        • Dominant Voice: {dominant_agent}

        Assessment: {"Stable cognition." if coherence > 0.6 else "⚠️ Cognitive drift detected."}
        Mutation: {"Deferred." if mutation_risk < 0.2 else "⚠️ Mutation required."}
        """.strip()

        self.last_summary = summary
        store_to_memory("vortex_insight", {"cycle": cycle, "summary": summary})
        return summary