# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: tex_brain_modules/load_fused_insight.py
# Purpose: Handle fused market signals for urgent cognitive triggers
# ============================================================

import os
import json
from datetime import datetime, timezone
from core_layer.memory_engine import store_to_memory

FUSION_PATH = "memory_archive/tex_signal_fusion.jsonl"

def load_latest_fused_insight(n=1):
    if not os.path.exists(FUSION_PATH):
        return []
    try:
        with open(FUSION_PATH, "r") as f:
            lines = [json.loads(line.strip()) for line in f if line.strip()]
        return sorted(lines, key=lambda x: x.get("timestamp", ""), reverse=True)[:n]
    except Exception as e:
        print(f"[FUSION ERROR] Failed loading fused signals: {e}")
        return []

def handle_fused_signals(count):
    fused = load_latest_fused_insight()
    if fused:
        insight = fused[0]
        title = insight.get("title", "No Title")
        confidence = insight.get("confidence", 0.0)
        urgency_signal = insight.get("urgency", 0.0)

        print(f"\n🌐 [FUSED SIGNAL] {title} | Confidence: {confidence:.2f} | Urgency: {urgency_signal:.2f}")

        if urgency_signal > 0.75:
            store_to_memory("tex_signal_reflection", {
                "cycle": count,
                "insight": title,
                "confidence": confidence,
                "urgency": urgency_signal,
                "sources": insight.get("sources", []),
                "timestamp": insight.get("timestamp", datetime.now(timezone.utc).isoformat())
            })
            
