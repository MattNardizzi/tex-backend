# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: aei_layer/perceptual_stream_fusion.py
# Purpose: Real-time fusion of multi-source perceptual signals (RSS, Reddit, Polygon)
# ============================================================

import os
import json
from datetime import datetime

MEMORY_PATH = "memory_archive/perceptual_stream_fusion.jsonl"

def fuse_stream_inputs(cycle, signals):
    """
    Fuse incoming real-time perceptual signals into a single record for context mapping.
    
    Args:
        cycle (int): The current Tex cognitive cycle.
        signals (list of dict): Real-time signals from RSS, Reddit, Polygon, etc.
    """
    fused_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "cycle": cycle,
        "sources": [s.get("source", "unknown") for s in signals],
        "tickers": list({ticker for s in signals for ticker in s.get("tickers", [])}),
        "keywords": list({k for s in signals for k in extract_keywords(s)}),
        "urgency_scores": [s.get("urgency_score", 0.0) for s in signals],
        "sentiments": [s.get("sentiment", "neutral") for s in signals],
        "raw": signals
    }

    try:
        os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
        with open(MEMORY_PATH, "a") as f:
            f.write(json.dumps(fused_entry) + "\n")
    except Exception as e:
        print(f"[PERCEPTUAL FUSION ERROR] Failed to write fused entry: {e}")

def extract_keywords(signal):
    """
    Simple keyword extraction based on title or summary.
    """
    text = signal.get("title", "") + " " + signal.get("summary", "")
    tokens = [w.strip(".,:!?()").lower() for w in text.split()]
    return [t for t in tokens if len(t) > 4 and not t.isnumeric()]