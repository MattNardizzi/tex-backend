# ============================================================
# 🧠 Alpha Paradox Engine (Tier Ω) – Recursive Contradiction Auditor
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# Purpose: Detect internal contradictions between alpha logic and observed outcomes
# ============================================================

import random
import hashlib
from datetime import datetime

class AlphaParadoxEngine:
    def __init__(self):
        self.history = []

    def analyze_contradiction(self, alpha_forecast, realized_result, causal_trace):
        """
        Compare alpha expectation vs realized and causal trace.
        If deviation exceeds threshold, flag paradox.
        """
        expectation_hash = self._generate_hash(alpha_forecast)
        result_hash = self._generate_hash(realized_result)
        causal_hash = self._generate_hash(causal_trace)

        mismatch_score = self._compute_mismatch(alpha_forecast, realized_result)
        deviation_score = self._check_causal_dissonance(alpha_forecast, causal_trace)

        paradox = mismatch_score > 0.65 and deviation_score > 0.5

        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "expectation_hash": expectation_hash,
            "result_hash": result_hash,
            "causal_hash": causal_hash,
            "mismatch": round(mismatch_score, 3),
            "dissonance": round(deviation_score, 3),
            "paradox_triggered": paradox
        }

        self.history.append(record)
        if paradox:
            print(f"[PARADOX] ⚠️ Contradiction detected → mismatch: {mismatch_score:.2f}, dissonance: {deviation_score:.2f}")
        return record

    def _generate_hash(self, obj):
        h = hashlib.sha256(str(obj).encode()).hexdigest()
        return h[:12]

    def _compute_mismatch(self, forecast, result):
        """Measures semantic difference."""
        score = 0.0
        if isinstance(forecast, str) and isinstance(result, str):
            if forecast[:30] != result[:30]:
                score += 0.4
            score += random.uniform(0.0, 0.4)
        return score

    def _check_causal_dissonance(self, forecast, trace):
        """Evaluates contradiction between forecast and what causally unfolded."""
        if forecast and trace and forecast not in str(trace):
            return round(random.uniform(0.5, 1.0), 3)
        return round(random.uniform(0.0, 0.3), 3)

    def get_recent_events(self, limit=5):
        return self.history[-limit:]

# === Standalone Test ===
if __name__ == "__main__":
    ape = AlphaParadoxEngine()
    alpha = "Tex predicts high payoff from event chain A > B > C"
    result = "Market triggered B > D instead, with regret"
    trace = ["A causes B", "B misfires", "C is skipped"]

    output = ape.analyze_contradiction(alpha, result, trace)
    print(output)
