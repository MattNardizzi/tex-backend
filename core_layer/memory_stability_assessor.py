# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/memory_stability_assessor.py
# Purpose: Monitor memory volatility and stability across cognitive cycles
# ============================================================

import os
import json
from datetime import datetime, timezone
from statistics import mean, stdev
from core_layer.memory_engine import recall_recent

STABILITY_LOG_PATH = "memory_archive/memory_stability_log.jsonl"

def assess_memory_stability(agent_name="tex", window=30):
    """
    Analyze volatility of Tex's thought score trends to detect mental instability patterns.
    """
    recent = recall_recent(n=window)
    scores = []

    for entry in recent:
        if "data" not in entry:
            continue
        score = entry["data"].get("score")
        if score is not None:
            scores.append(score)

    if len(scores) < 5:
        return {"message": "Insufficient data to assess memory stability."}

    avg_score = round(mean(scores), 3)
    std_dev = round(stdev(scores), 3)

    stability_report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": agent_name,
        "average_score": avg_score,
        "score_volatility": std_dev,
        "memory_window": len(scores)
    }

    _log_stability(stability_report)
    return stability_report

def _log_stability(report):
    """
    Logs stability reports safely into memory_archive.
    """
    try:
        with open(STABILITY_LOG_PATH, "a") as f:
            f.write(json.dumps(report) + "\n")
        print(f"[STABILITY MONITOR] 📊 Logged stability report: Avg={report['average_score']}, Volatility={report['score_volatility']}")
    except Exception as e:
        print(f"[STABILITY ERROR] ❌ Failed logging stability: {e}")

# === Standalone CLI Debug
if __name__ == "__main__":
    report = assess_memory_stability()
    print(report)