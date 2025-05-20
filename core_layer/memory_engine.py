# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/memory_engine.py
# Purpose: Robust agent-based memory engine for AGI systems
# ============================================================

import os
import json
from datetime import datetime, timezone, timedelta

# === In-memory short-term recall (RAM only)
_memory_log = []

# === Memory Directory Setup
MEMORY_DIR = "memory_archive"
os.makedirs(MEMORY_DIR, exist_ok=True)

# === Unified Memory Writer
def store_to_memory(agent_name, data):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": agent_name,
        "data": data
    }

    filepath = os.path.join(MEMORY_DIR, f"{agent_name}.jsonl")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    try:
        with open(filepath, "a") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[MEMORY] 🧠 Stored for {agent_name}: {data}")
    except Exception as e:
        print(f"[MEMORY ERROR] ❌ Failed saving for {agent_name}: {e}")

    _memory_log.append(entry)
    return entry

# === Recall last N memory entries for an agent (from disk)
def recall_agent_memory(agent_name, n=5):
    filepath = os.path.join(MEMORY_DIR, f"{agent_name}.jsonl")
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
            return [json.loads(line) for line in lines[-n:] if line.strip()]
    except Exception as e:
        print(f"[MEMORY ERROR] ❌ Recall failed for {agent_name}: {e}")
        return []

# === Recall the latest single memory entry for an agent
def recall_latest(agent_name):
    history = recall_agent_memory(agent_name, n=1)
    return history[0] if history else None

# === Recall short-term RAM memory (optional time filter)
def recall_recent(n=5, within_minutes=None):
    print(f"[MEMORY] 🔁 Recalling {n} recent in-session memories (within {within_minutes} min)...")
    memories = _memory_log[-n:]

    if within_minutes is not None:
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=within_minutes)
        filtered = []
        for entry in memories:
            try:
                ts = datetime.fromisoformat(entry.get("timestamp"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
                if ts >= cutoff:
                    filtered.append(entry)
            except Exception as e:
                print(f"[MEMORY WARNING] ⚠️ Bad timestamp skipped: {e}")
        memories = filtered

    return memories

# === Recall ALL memory entries safely from disk
def recall_all(agent_name):
    filepath = os.path.join(MEMORY_DIR, f"{agent_name}.jsonl")
    if not os.path.exists(filepath):
        return []

    memory_entries = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    memory_entries.append(json.loads(line))
                except json.JSONDecodeError:
                    print(f"[MEMORY WARNING] ⚠️ Skipping corrupted memory line.")
    except Exception as e:
        print(f"[MEMORY ERROR] ❌ Full recall failed for {agent_name}: {e}")

    return memory_entries

# === ✅ Tier 8.5: Rewrite Incorrect Memories ===
def rewrite_memory_entry(domain, original_reasoning, replacement):
    path = os.path.join(MEMORY_DIR, f"{domain}.jsonl")
    if not os.path.exists(path):
        return False

    new_lines = []
    rewritten = False
    with open(path, "r") as f:
        for line in f:
            entry = json.loads(line.strip())
            if entry.get("data", {}).get("reasoning") == original_reasoning:
                entry["data"]["reasoning"] = replacement
                entry["data"]["revised_at"] = datetime.utcnow().isoformat()
                entry["data"]["note"] = "rewritten due to contradiction or regret"
                rewritten = True
            new_lines.append(json.dumps(entry))

    if rewritten:
        with open(path, "w") as f:
            f.write("\n".join(new_lines) + "\n")
    return rewritten

# === ✅ Tier 8.5: Annotate Memory Instead of Rewriting ===
def annotate_memory(domain, original_reasoning, annotation):
    path = os.path.join(MEMORY_DIR, f"{domain}.jsonl")
    if not os.path.exists(path):
        return False

    new_lines = []
    annotated = False
    with open(path, "r") as f:
        for line in f:
            entry = json.loads(line.strip())
            if entry.get("data", {}).get("reasoning") == original_reasoning and "note" not in entry.get("data", {}):
                entry["data"]["note"] = annotation
                entry["data"]["annotated_at"] = datetime.utcnow().isoformat()
                annotated = True
            new_lines.append(json.dumps(entry))

    if annotated:
        with open(path, "w") as f:
            f.write("\n".join(new_lines) + "\n")
    return annotated