# ============================================================
# © 2025 VortexBlack LLC. All rights reserved.
# File: core_layer/heartbeat_monitor.py
# Purpose: Monitors cognitive heartbeat of core agents
# ============================================================

import os
import json
from datetime import datetime, timezone

MEMORY_DIR = "memory_archive"
AGENTS = ["tex", "AeonDelta", "tex_child_001", "tex_child_002"]
TIMEOUT_SECONDS = 300  # Alert if no update in last 5 minutes

def read_latest_timestamp(agent_name):
    file_path = os.path.join(MEMORY_DIR, f"{agent_name}.jsonl")
    if not os.path.exists(file_path):
        return None

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            if not lines:
                return None
            last_entry = json.loads(lines[-1])
            return last_entry.get("timestamp")
    except Exception as e:
        print(f"[HEARTBEAT] ⚠️ Failed to read {agent_name}: {e}")
        return None

def parse_timestamp(ts_str):
    try:
        ts = datetime.fromisoformat(ts_str)
        if ts.tzinfo is None:
            return ts.replace(tzinfo=timezone.utc)
        return ts
    except Exception as e:
        print(f"[HEARTBEAT ERROR] Failed to parse timestamp: {ts_str} → {e}")
        return None

def check_heartbeats():
    print("❤️ [HEARTBEAT MONITOR] Checking agent activity...\n")
    now = datetime.now(timezone.utc)

    for agent in AGENTS:
        ts_str = read_latest_timestamp(agent)
        if not ts_str:
            print(f"❓ {agent}: No memory logged yet.")
            continue

        ts = parse_timestamp(ts_str)
        if not ts:
            print(f"⚠️ {agent}: Invalid timestamp.")
            continue

        delta = (now - ts).total_seconds()
        if delta > TIMEOUT_SECONDS:
            print(f"🔴 {agent}: INACTIVE for {round(delta / 60, 1)} min")
        else:
            print(f"🟢 {agent}: Active ({round(delta)}s ago)")

if __name__ == "__main__":
    check_heartbeats()