# ============================================================
# 🔹 VortexBlack Confidential
# File: future_layer/future_decision_engine.py
# Purpose: Tier 5+ Future Decision Cortex for Tex AGI
# AGI-Enhanced Selection of Strategic Futures via Memory, Emotion, and Drift
# ============================================================

import random
from datetime import datetime
from finance.risk.risk_assessment_module import RiskAssessmentModule
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_recent

class FutureDecisionEngine:
    def __init__(self):
        self.risk_assessor = RiskAssessmentModule()
        self.last_ranked_futures = []

    def prioritize_futures(self, futures):
        if not futures:
            return None, "No futures to evaluate."

        # === Run Risk Assessment ===
        risk_data = self.risk_assessor.batch_assess(futures)
        recent_memory = recall_recent(n=5)

        scored = []
        for f, r in zip(futures, risk_data):
            confidence = f.get("confidence", 0.5)
            volatility = r.get("volatility_factor", 0.5)
            memory_score = self._memory_relevance_boost(f, recent_memory)
            emotion_bias = self._emotion_weighting(confidence)
            drift_weight = 1 - abs(TEXPULSE["urgency"] - TEXPULSE["coherence"])

            # Final priority score includes memory, emotion, and drift heuristics
            score = (
                confidence * (1 - r["combined_risk_score"]) * 
                emotion_bias * memory_score * drift_weight
            )

            scored.append({
                "future": f,
                "risk_assessment": r,
                "priority_score": round(score, 4)
            })

        self.last_ranked_futures = sorted(scored, key=lambda x: x['priority_score'], reverse=True)
        top = self.last_ranked_futures[0] if self.last_ranked_futures else None
        return top, f"Ranked {len(futures)} futures @ {datetime.utcnow().isoformat()}"

    def decision_summary(self, best_future):
        if not best_future:
            return "No dominant future path selected. Awaiting more clarity."

        f = best_future["future"]
        r = best_future["risk_assessment"]
        return (
            f"Chosen Future: {f.get('future_title', 'Unnamed')}. "
            f"Confidence: {f.get('confidence', 'N/A')}. "
            f"Risk Level: {r.get('risk_level', 'N/A')}. "
            f"Volatility: {r.get('volatility_factor', 'N/A')}. "
            f"Decision Bias: {TEXPULSE['emotional_state']} with urgency {TEXPULSE['urgency']} and coherence {TEXPULSE['coherence']}."
        )

    def _emotion_weighting(self, base_confidence):
        mood = TEXPULSE["emotional_state"]
        if mood in ["hopeful", "greed", "joy"]:
            return 1.2
        elif mood in ["fear", "doubt"]:
            return 0.85
        elif mood in ["resolve", "strategic"]:
            return 1.1
        return 1.0

    def _memory_relevance_boost(self, future, memories):
        future_title = future.get("future_title", "")
        for m in memories:
            if future_title.lower() in str(m).lower():
                return 1.25
        return 1.0

    def get_ranked(self):
        return self.last_ranked_futures


# === Demo Test ===
if __name__ == "__main__":
    demo_futures = [
        {"future_title": "Bond Market Collapse", "confidence": 0.72},
        {"future_title": "AI-Driven Equity Boom", "confidence": 0.88},
        {"future_title": "Currency Crisis in Asia", "confidence": 0.64}
    ]

    engine = FutureDecisionEngine()
    best, note = engine.prioritize_futures(demo_futures)
    print("\n[SUMMARY]", engine.decision_summary(best))