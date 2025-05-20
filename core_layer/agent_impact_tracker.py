# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/agent_impact_tracker.py
# Purpose: Track agent impact scores across time in two files
# ============================================================

import os
import json
from datetime import datetime, timezone

# === File Paths ===
IMPACT_SUMMARY_FILE = "memory_archive/agent_impact_summary.json"
IMPACT_LOG_FILE = "memory_archive/agent_impact_scores.jsonl"

# Ensure memory directory exists
os.makedirs("memory_archive", exist_ok=True)

def log_agent_impact(agent_id, score, reasoning_summary):
    timestamp = datetime.now(timezone.utc).isoformat()

    # === Rolling .jsonl log entry
    log_entry = {
        "timestamp": timestamp,
        "agent_id": agent_id,
        "score": round(score, 4),
        "reasoning_summary": reasoning_summary
    }

    try:
        with open(IMPACT_LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
        print(f"[IMPACT TRACKER] 📄 Logged agent impact → {agent_id} ({score})")
    except Exception as e:
        print(f"[IMPACT ERROR] ❌ Failed to log agent impact: {e}")

    # === Update cumulative impact summary
    summary_data = {}
    if os.path.exists(IMPACT_SUMMARY_FILE):
        try:
            with open(IMPACT_SUMMARY_FILE, "r") as f:
                summary_data = json.load(f)
        except Exception:
            print("[IMPACT WARNING] ⚠️ Failed to load previous summary. Starting fresh.")

    if agent_id not in summary_data:
        summary_data[agent_id] = {
            "total_score": 0,
            "entries": 0,
            "average_score": 0
        }

    summary_data[agent_id]["total_score"] += score
    summary_data[agent_id]["entries"] += 1
    summary_data[agent_id]["average_score"] = round(
        summary_data[agent_id]["total_score"] / summary_data[agent_id]["entries"], 4
    )

    try:
        with open(IMPACT_SUMMARY_FILE, "w") as f:
            json.dump(summary_data, f, indent=2)
        print(f"[IMPACT TRACKER] ✅ Updated summary for {agent_id}")
    except Exception as e:
        print(f"[IMPACT ERROR] ❌ Failed to update summary: {e}")

# === CLI TEST (optional)
if __name__ == "__main__":
    print("🧠 Testing agent impact tracker...")
    log_agent_impact("debate_001", 0.82, "Sample reasoning: logical + hopeful")