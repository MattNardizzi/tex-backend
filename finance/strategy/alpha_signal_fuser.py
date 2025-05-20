# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: finance/strategy/alpha_signal_fuser.py
# Purpose: Tier 12 — Fuse Alpha Signals into Long-Term Memory + Drift-Aware Feedback
# ============================================================

from core_layer.memory_engine import store_to_memory, recall_agent_memory
from datetime import datetime
import uuid

class AlphaSignalFuser:
    def __init__(self, memory_agent="alpha_signals"):
        self.agent = memory_agent

    def fuse_signals(self, alpha_rationale, strategy, performance=None):
        fused_id = str(uuid.uuid4())
        signal_packet = {
            "id": fused_id,
            "timestamp": datetime.utcnow().isoformat(),
            "rationale": alpha_rationale,
            "strategy": strategy,
            "performance": performance or {},
            "fusion_type": "tier_12_feedback"
        }
        store_to_memory(self.agent, signal_packet)
        print(f"[FUSION] ✅ Stored Alpha Signal → ID: {fused_id}")
        return fused_id

    def recall_recent_signals(self, n=5):
        return recall_agent_memory(self.agent, n)

    def summarize_alpha_trends(self, n=10):
        entries = recall_agent_memory(self.agent, n)
        trends = [f"→ {e['timestamp']}: {e['rationale']}" for e in entries if 'rationale' in e]
        return "\n".join(trends) or "No recent alpha signals."


# === Test Harness ===
if __name__ == "__main__":
    fuser = AlphaSignalFuser()
    fused = fuser.fuse_signals(
        alpha_rationale="High-growth tech rotation justified by liquidity contraction",
        strategy=["AAPL", "NVDA", "MSFT"],
        performance={"gain": 0.12, "volatility": 0.04}
    )

    print("\n[ALPHA SIGNALS]")
    for s in fuser.recall_recent_signals():
        print(s)

    print("\n[SUMMARY]")
    print(fuser.summarize_alpha_trends())
