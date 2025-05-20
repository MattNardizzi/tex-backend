# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/cognitive_drift_monitor.py
# Purpose: Detect cognitive drift and deviation from original Tex Manifest
# ============================================================

import os
import json
from datetime import datetime, timezone
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_recent

DRIFT_LOG_PATH = "memory_archive/cognitive_drift_log.jsonl"

def assess_drift(agent_name="tex", window=20):
    """
    Analyzes Tex's recent memories to detect drift away from his core manifest identity (TEXPULSE codename).
    """
    recent_memories = recall_recent(n=window)
    manifest_identity = TEXPULSE.get("codename", "Tex")
    deviations = []

    for entry in recent_memories:
        if not entry or "data" not in entry:
            continue
        explanation = entry["data"].get("explanation", "")
        if explanation and manifest_identity.lower() not in explanation.lower():
            deviations.append({
                "timestamp": entry.get("timestamp", datetime.now(timezone.utc).isoformat()),
                "explanation": explanation
            })

    drift_ratio = round(len(deviations) / max(1, len(recent_memories)), 2)

    drift_report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": agent_name,
        "drift_ratio": drift_ratio,
        "deviation_count": len(deviations),
        "scanned_memories": len(recent_memories),
        "deviations": deviations
    }

    _log_drift_report(drift_report)
    return drift_report

def detect_cognitive_stall(similarity, patch_payload, outcome_score):
    """
    Detects if Tex is cognitively stalling based on:
    - Similarity to last memory
    - Weak patch decision
    - Poor outcome scores
    """
    if similarity < 0.6 and outcome_score < 0.0:
        return True
    if patch_payload.get("strategy", "none") == "none" and outcome_score < 0.0:
        return True
    return False

def _log_drift_report(report):
    """
    Logs drift reports into cognitive_drift_log.jsonl safely.
    """
    try:
        os.makedirs(os.path.dirname(DRIFT_LOG_PATH), exist_ok=True)
        with open(DRIFT_LOG_PATH, "a") as f:
            f.write(json.dumps(report) + "\n")
        print(f"[DRIFT MONITOR] 📉 Logged drift ratio: {report['drift_ratio']} (Deviations: {report['deviation_count']})")
    except Exception as e:
        print(f"[DRIFT MONITOR ERROR] ❌ Failed to log drift report: {e}")

# === Standalone CLI Debugging
if __name__ == "__main__":
    report = assess_drift()
    print(json.dumps(report, indent=2))