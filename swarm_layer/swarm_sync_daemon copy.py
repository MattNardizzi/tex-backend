# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: swarm_layer/swarm_sync_daemon.py
# Purpose: Daemon that continuously syncs swarm agents and reports drift back to Tex
# ============================================================

import os
import json
import time
from datetime import datetime
from core_layer.memory_engine import store_to_memory

SWARM_FEED      = "memory_archive/swarm_feed.jsonl"
CHILD_SPAWN_LOG = "memory_archive/child_spawn_log.jsonl"


class SwarmSyncDaemon:
    def __init__(self, interval: int = 60):
        self.interval = interval  # seconds between syncs
        self._last_snapshot = None  # for deduplication check
        print("[✅ SWARM SYNC DAEMON] Hardened version loaded (valid_agents enforced)")

    # ──────────────────────────────────────────────────────────
    # CHILD AGENT LOADER
    # ──────────────────────────────────────────────────────────
    def _load_child_agents(self):
        if not os.path.exists(CHILD_SPAWN_LOG):
            return []

        valid_agents = []
        with open(CHILD_SPAWN_LOG, "r") as f:
            for idx, line in enumerate(f):
                try:
                    agent = json.loads(line.strip())
                    if isinstance(agent, dict):
                        valid_agents.append(agent)
                    else:
                        print(f"[SWARM SYNC WARNING] Non-dict agent at index {idx}")
                        store_to_memory("swarm_sync_errors", {
                            "timestamp": datetime.utcnow().isoformat(),
                            "index": idx,
                            "bad_type": str(type(agent)),
                            "raw_value": str(agent)[:300],
                        })
                except Exception as e:
                    print(f"[SWARM SYNC WARNING] Malformed JSON at line {idx}: {e}")
        return valid_agents

    # ──────────────────────────────────────────────────────────
    # SNAPSHOT GENERATOR
    # ──────────────────────────────────────────────────────────
    def _generate_swarm_snapshot(self, agents):
        # 🔒 Step 1 – filter malformed agent entries
        valid_agents = []
        for idx, a in enumerate(agents):
            if isinstance(a, dict):
                valid_agents.append(a)
            else:
                print(f"[SWARM SYNC WARNING] Skipping malformed agent at index {idx}: "
                      f"{type(a).__name__}")
                store_to_memory("swarm_sync_errors", {
                    "timestamp": datetime.utcnow().isoformat(),
                    "index": idx,
                    "bad_type": str(type(a)),
                    "raw_value": str(a)[:300],
                })

        # 🔒 Step 2 – collect emotions & biases with fallback for string shorthands
        emotions, biases = [], []
        for idx, agent in enumerate(valid_agents):
            traits = agent.get("traits")

            # ── Fallback A: traits provided as a simple string
            if isinstance(traits, str):
                t = traits.lower()
                traits = {}
                if t in {
                    "fear", "hope", "resolve", "doubt",
                    "greed", "curiosity", "anger", "joy"
                }:
                    traits["emotion"] = t
                else:                       # treat as bias label
                    traits["bias"] = t

            # ── Fallback B: traits not a dict and not a string → skip entry
            if not isinstance(traits, dict):
                print(f"[SWARM SYNC WARNING] Malformed traits for agent "
                      f"{agent.get('id', '?')} — skipping")
                store_to_memory("swarm_sync_errors", {
                    "timestamp":  datetime.utcnow().isoformat(),
                    "issue":      "non-dict traits",
                    "agent_index": idx,
                    "raw_traits":  str(traits)[:300],
                })
                continue

            emotions.append(traits.get("emotion", "unknown"))
            biases.append(traits.get("bias", "neutral"))

        # 🔒 Step 3 – assemble final snapshot
        summary = {
            "timestamp":              datetime.utcnow().isoformat(),
            "swarm_size":             len(valid_agents),
            "emotional_distribution": {e: emotions.count(e) for e in set(emotions)},
            "bias_distribution":      {b: biases.count(b)   for b in set(biases)},
        }
        return summary

    # ──────────────────────────────────────────────────────────
    # MAIN LOOP
    # ──────────────────────────────────────────────────────────
    def run(self):
        print("[SWARM SYNC DAEMON] 🧠 Syncing swarm state...")
        while True:
            try:
                agents   = self._load_child_agents()
                snapshot = self._generate_swarm_snapshot(agents)

                # extra guard — snapshot must be a dict
                if not isinstance(snapshot, dict):
                    print("[SWARM SYNC DAEMON] ⚠️ Malformed snapshot — expected dict, got "
                          f"{type(snapshot).__name__}")
                    time.sleep(self.interval)
                    continue

                # 🛑 New Guard: Avoid writing duplicate snapshots
                if snapshot == self._last_snapshot:
                    time.sleep(self.interval)
                    continue
                self._last_snapshot = snapshot

                with open(SWARM_FEED, "a") as f:
                    f.write(json.dumps(snapshot) + "\n")

                store_to_memory("swarm_feed", snapshot)
                print(f"[SWARM SYNC] ✅ Snapshot stored @ {snapshot['timestamp']}")
            except Exception as e:
                print(f"[SWARM SYNC ERROR] {e}")

            time.sleep(self.interval)