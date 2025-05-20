# ============================================================
# 🔹 VortexBlack Confidential
# File: alpha_explainer.py
# Purpose: Tex Autonomous Alpha Explainer (Tier 5 AGI Narrative Layer)
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# ============================================================

import random
import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_latest
from finance.execution.market_action_engine import MarketActionEngine
from finance.risk.risk_assessment_module import RiskAssessmentModule
from finance.strategy.portfolio_thinker import PortfolioThinker
from core_layer.goal_engine import get_active_goals
from tex_children.aeondelta import get_swarm_emotion_distribution

class AlphaExplainer:
    def __init__(self):
        self.market_engine = MarketActionEngine()
        self.risk_module = RiskAssessmentModule()
        self.portfolio_ai = PortfolioThinker()
        self.swarm_emotion = get_swarm_emotion_distribution
        self.explainer_memory = []

    def explain_alpha_origin(self, futures, market_context=None):
        """
        Returns a detailed self-narrated explanation of why Tex selected a particular alpha strategy.
        """
        if not futures:
            return "No future scenarios provided for alpha explanation."

        top_action = self.market_engine.decide_action(
            futures,
            emotion=TEXPULSE.get("emotional_state", "neutral"),
            urgency=TEXPULSE.get("urgency", 0.5),
            coherence=TEXPULSE.get("coherence", 0.5)
        )

        top_risks = self.risk_module.batch_assess(futures)
        portfolio = self.portfolio_ai.build_adaptive_portfolio(futures)
        memory_trace = recall_latest(limit=1)

        emotion = TEXPULSE.get("emotional_state")
        urgency = TEXPULSE.get("urgency")
        coherence = TEXPULSE.get("coherence")
        swarm_mood = self.swarm_emotion()

        rationale = f"""
        [ALPHA EXPLANATION REPORT]
        Cycle Timestamp: {datetime.utcnow().isoformat()}
        
        ➤ Dominant Emotion: {emotion}
        ➤ Cognitive Urgency: {urgency}
        ➤ Alignment Coherence: {coherence}
        ➤ Swarm Mood: {swarm_mood}
        
        ➤ Chosen Strategy: {top_action['action']} on "{top_action['future']}"
        ➤ Reasoning Bias: {top_action['bias']}
        ➤ Risk Level: {top_risks[0]['risk_level']} (Volatility: {top_risks[0]['volatility_factor']})
        ➤ Memory Context: {memory_trace[0]['data']['explanation'] if memory_trace else 'No memory trace found.'}
        
        ➤ Portfolio Constructed: {[a['title'] for a in portfolio['assets']]} (Diversity: {portfolio['diversity_index']})
        ➤ Final Confidence Score: {top_action['confidence']}
        
        Tex selected this approach based on emotional modulation, memory-driven awareness, and real-time swarm feedback. 
        Confidence is further reinforced via mutation awareness and future volatility projections.
        """

        self.explainer_memory.append({
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "report": rationale.strip()
        })

        return rationale.strip()

    def get_recent_explanations(self, limit=3):
        return self.explainer_memory[-limit:]

# === Usage Test ===
if __name__ == "__main__":
    explainer = AlphaExplainer()
    mock_futures = [
        {"future_title": "Oil Shock Recovery", "confidence": 0.76, "urgency": 0.7, "coherence": 0.8},
        {"future_title": "AI-led Boom", "confidence": 0.88, "urgency": 0.85, "coherence": 0.72}
    ]
    explanation = explainer.explain_alpha_origin(mock_futures)
    print(explanation)
