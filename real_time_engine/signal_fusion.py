# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: real_time_engine/signal_fusion.py
# Purpose: Fuses incoming real-time signals into high-confidence insights
# ============================================================

import time
import hashlib
import json
from datetime import datetime, timezone
from core_layer.memory_engine import store_to_memory

# === Global signal buffer
signal_buffer = []

# === Register incoming signal
def register_signal(signal):
    signal_buffer.append(signal)

# === Fuse logic with deduplication + confidence weighting
def fuse_signals():
    fused = {}

    for signal in signal_buffer:
        key = signal["title"].lower().strip()

        if key not in fused:
            fused[key] = {
                "title": signal["title"],
                "sources": [signal["source"]],
                "urgency": signal["urgency"],
                "count": 1,
                "timestamp": signal["timestamp"]
            }
        else:
            fused[key]["sources"].append(signal["source"])
            fused[key]["urgency"] += signal["urgency"]
            fused[key]["count"] += 1

    insights = []

    for key, data in fused.items():
        confidence = round(min(1.0, 0.3 + 0.15 * data["count"]), 2)
        avg_urgency = round(data["urgency"] / data["count"], 2)

        # Unique ID using title + timestamp
        unique_string = f"{data['title']}{data['timestamp']}"
        insight_id = hashlib.sha256(unique_string.encode()).hexdigest()[:12]

        insight = {
            "id": insight_id,
            "type": "insight",
            "title": data["title"],
            "sources": list(set(data["sources"])),
            "confidence": confidence,
            "urgency": avg_urgency,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        insights.append(insight)

    return insights

# === Execute signal fusion cycle
def run_fusion_cycle():
    print("🔁 [FUSION] Starting signal fusion cycle...")

    if not signal_buffer:
        print("🔕 [FUSION] No signals received this cycle.")
        return

    insights = fuse_signals()
    print(f"🧠 [FUSION] {len(insights)} fused insights created.")

    for insight in insights:
        print(f"📡 Insight: {insight['title']} (confidence: {insight['confidence']})")
        store_to_memory("tex_signal_fusion", insight)

    signal_buffer.clear()

# === Debug CLI Test
if __name__ == "__main__":
    test_signals = [
        {
            "title": "AI stock surge",
            "source": "twitter",
            "urgency": 0.75,
            "timestamp": datetime.now(timezone.utc).isoformat()
        },
        {
            "title": "AI stock surge",
            "source": "newsapi",
            "urgency": 0.65,
            "timestamp": datetime.now(timezone.utc).isoformat()
        },
        {
            "title": "Crypto crash",
            "source": "rss",
            "urgency": 0.9,
            "timestamp": datetime.now(timezone.utc).isoformat()
        },
    ]

    for sig in test_signals:
        register_signal(sig)

    run_fusion_cycle()