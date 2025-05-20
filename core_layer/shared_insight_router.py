# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: shared_insight_router.py
# Purpose: Routes insights across active agents in real-time
# ============================================================

import os
import json
import time
from datetime import datetime, timezone
from core_layer.memory_engine import store_to_memory

# === Config
ROUTER_LOG = "memory_archive/insight_broadcast.log"
AGENTS = ["Tex", "AeonDelta", "TEX-CHILD-001", "Tex_Child_002"]

# === Broadcast insight across all known agents
def broadcast_insight(insight, origin="Tex"):
    timestamp = datetime.now(timezone.utc).isoformat()
    for agent in AGENTS:
        if agent != origin:
            routed = {
                "type": "broadcast",
                "origin": origin,
                "target": agent,
                "insight": insight,
                "timestamp": timestamp
            }
            store_to_memory("shared_insights", routed)
            log_insight(routed)
            print(f"📡 Routed → {agent}: {insight.get('title', '[No Title]')}")

# === Log broadcast for tracking
def log_insight(entry):
    os.makedirs(os.path.dirname(ROUTER_LOG), exist_ok=True)
    with open(ROUTER_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

# === Manual Debug Mode
if __name__ == "__main__":
    test_insight = {
        "title": "Volatility Spike in TSLA",
        "confidence": 0.92,
        "urgency": 0.87,
        "source": "polygon_stream"
    }
    broadcast_insight(test_insight, origin="Tex")