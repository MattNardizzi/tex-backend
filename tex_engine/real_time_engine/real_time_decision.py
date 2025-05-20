# ============================================================
# Tex Real-Time Decision Engine – Data Fusion Layer
# ============================================================

from real_time_engine.rss_stream import RSSStream
from agentic_ai.reasoning_trace import log_reasoning_step
import random
import time

class RealTimeDecisionEngine:
    def __init__(self):
        self.rss = RSSStream()

    def evaluate_environment(self):
        print("[REAL-TIME] ⚡ Evaluating incoming signals...")
        signals = self.rss.fetch_headlines()
        fused_insights = []
        for s in signals:
            enriched = self.rss.simulate_relevance(s)
            fused_insights.append(enriched)
        return fused_insights

    def run(self):
        print("[REAL-TIME] ✅ Engine online. Listening for signals...")
        while True:
            insights = self.evaluate_environment()
            for item in insights:
                title = item.get("title", "")
                score = item.get("urgency_score", 0)

                if score > 0.7:
                    decision = "Take action based on critical signal"
                    print(f"[DECISION] ⚠️ HIGH PRIORITY: {title} → Action Needed!")
                else:
                    decision = "No immediate action – continue monitoring"
                    print(f"[DECISION] 📊 Monitoring: {title}")

                # Log the reasoning trace for every insight
                log_reasoning_step(
                    source="real_time_decision.py",
                    input_text=title,
                    output_text=decision,
                    confidence=round(score, 2),
                    agent="Tex"
                )

            time.sleep(10)