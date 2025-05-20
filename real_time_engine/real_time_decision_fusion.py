# ============================================================
# Real-Time Decision Fusion – Streaming Signal Integration
# ============================================================

import random

class RealTimeDecisionFusion:
    def __init__(self):
        self.latest_signals = []

    def ingest_stream_data(self, sentiment_score, volatility_index, news_urgency):
        signal_strength = (sentiment_score * 0.4) + (volatility_index * 0.3) + (news_urgency * 0.3)
        self.latest_signals.append(signal_strength)
        print(f"[DECISION FUSION] 📡 Signal strength: {signal_strength:.3f}")

        if signal_strength > 0.75:
            return "BUY"
        elif signal_strength < 0.4:
            return "SELL"
        else:
            return "HOLD"
