# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/portfolio_explainer.py
# Purpose: Narrates Tex's portfolio reasoning with emotional context
# ============================================================

from core_layer.tex_manifest import TEXPULSE

def explain_portfolio_decision(self, alpha_rationale, strategy, foresight, regret_score):
    narration = f"""📈 [STRATEGY SUMMARY]
    Emotion: {TEXPULSE.get("emotional_state")}
    Urgency: {TEXPULSE.get("urgency")}
    Coherence: {TEXPULSE.get("coherence")}
    Confidence: {foresight.get('confidence', 'n/a')}
    Regret: {regret_score}
    Weights: {strategy.get('weights') if isinstance(strategy, dict) else 'N/A'}
    Reasoning: {alpha_rationale}
    """
    self.speak(narration.strip(), emotion=TEXPULSE.get("emotional_state", "neutral"))
    return narration.strip()