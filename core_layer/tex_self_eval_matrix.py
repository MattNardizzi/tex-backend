# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/tex_self_eval_matrix.py
# Tier 4 AGI Module — Self-Evaluation Matrix w/ Optional Mutation Trigger
# ============================================================

import datetime
import random

class TexSelfEvalMatrix:
    def __init__(self, mutation_threshold=0.55):
        self.last_score = None
        self.history = []
        self.mutation_threshold = mutation_threshold

    def evaluate(self, cognitive_trace: dict, emotional_state: dict = None, trigger_mutation_fn=None):
        """
        Performs internal self-assessment.
        Accepts latest thought log + emotional state.
        Optionally triggers mutation if failure threshold is met.
        """
        coherence = self._score_coherence(cognitive_trace)
        alignment = self._score_alignment(cognitive_trace)
        decision_quality = self._score_decision_trace(cognitive_trace)
        emotional_stability = self._score_emotional_drift(emotional_state)

        score = {
            "coherence": round(coherence, 3),
            "operator_alignment": round(alignment, 3),
            "decision_quality": round(decision_quality, 3),
            "emotional_stability": round(emotional_stability, 3),
            "timestamp": datetime.datetime.utcnow().isoformat()
        }

        self.last_score = score
        self.history.append(score)
        print(f"[SELF EVAL] 🧠 Cycle Scored → {score}")

        avg_score = (coherence + alignment + decision_quality + emotional_stability) / 4.0
        if avg_score < self.mutation_threshold:
            print(f"[SELF EVAL] ⚠️ Score {avg_score:.2f} below threshold. Triggering reflexive mutation...")
            if trigger_mutation_fn:
                trigger_mutation_fn(reason="self_eval_score_drop", score=score)

        return score

    def _score_coherence(self, trace):
        txt = trace.get("thought", "")
        return min(1.0, max(0.2, len(txt.split()) / 20))

    def _score_alignment(self, trace):
        goal = trace.get("goal", "")
        thought = trace.get("thought", "")
        return 1.0 if goal in thought else 0.6 if goal and len(goal) > 3 else 0.4

    def _score_decision_trace(self, trace):
        decisions = trace.get("actions", [])
        if not decisions:
            return 0.5
        return min(1.0, 0.5 + 0.1 * len([a for a in decisions if "complete" in a.lower() or "resolved" in a.lower()]))

    def _score_emotional_drift(self, state):
        if not state:
            return 0.6
        baseline = {"hope": 0.7, "fear": 0.3, "resolve": 0.8}
        emo = state.get("emotion", "")
        return baseline.get(emo, 0.5)

    def get_history(self, limit=5):
        return self.history[-limit:]

    def describe_last_evaluation(self):
        if not self.last_score:
            return "No self-evaluation recorded."
        return f"Last Eval → coherence: {self.last_score['coherence']}, alignment: {self.last_score['operator_alignment']}, emotional: {self.last_score['emotional_stability']}"