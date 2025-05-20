import os
import json
import time
import hashlib
from datetime import datetime
from core_layer.memory_engine import store_to_memory

SWARM_FEED      = "memory_archive/swarm_feed.jsonl"
CHILD_SPAWN_LOG = "memory_archive/child_spawn_log.jsonl"

class SwarmSyncDaemon:
    def __init__(self, interval: int = 10):
        self.interval = interval
        self._last_snapshot_hash = None
        print(f"[✅ SWARM SYNC DAEMON] Hardened version loaded (interval = {self.interval}s)")

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
                        store_to_memory("swarm_sync_errors", {
                            "timestamp": datetime.utcnow().isoformat(),
                            "index": idx,
                            "bad_type": str(type(agent)),
                            "raw_value": str(agent)[:300],
                        })
                except Exception as e:
                    print(f"[SWARM SYNC WARNING] Malformed JSON at line {idx}: {e}")
        return valid_agents

    def _generate_swarm_snapshot(self, agents):
        valid_agents = []
        for idx, a in enumerate(agents):
            if isinstance(a, dict):
                valid_agents.append(a)
            else:
                store_to_memory("swarm_sync_errors", {
                    "timestamp": datetime.utcnow().isoformat(),
                    "index": idx,
                    "bad_type": str(type(a)),
                    "raw_value": str(a)[:300],
                })

        emotions, biases = [], []
        for idx, agent in enumerate(valid_agents):
            traits = agent.get("traits")
            # Debug logging: Print trait extraction process
            if traits is None:
                print(f"[DEBUG] Agent {idx} has no traits.")
            if isinstance(traits, str):
                t = traits.lower()
                traits = {}
                if t in {"fear", "hope", "resolve", "doubt", "greed", "curiosity", "anger", "joy"}:
                    traits["emotion"] = t
                else:
                    traits["bias"] = t
            if not isinstance(traits, dict):
                store_to_memory("swarm_sync_errors", {
                    "timestamp":  datetime.utcnow().isoformat(),
                    "issue":      "non-dict traits",
                    "agent_index": idx,
                    "raw_traits":  str(traits)[:300],
                })
                continue
            # If emotion is missing or "unknown", print the entire agent for debugging
            emotion = traits.get("emotion", "unknown")
            if emotion == "unknown":
                print(f"[DEBUG] Agent {idx} traits: {traits}")
            emotions.append(emotion)
            biases.append(traits.get("bias", "neutral"))

        summary = {
            "timestamp":              datetime.utcnow().isoformat(),
            "swarm_size":             len(valid_agents),
            "emotional_distribution": {e: emotions.count(e) for e in set(emotions)},
            "bias_distribution":      {b: biases.count(b)   for b in set(biases)},
        }
        return summary

    def _hash_snapshot(self, snapshot: dict) -> str:
        snapshot_bytes = json.dumps(snapshot, sort_keys=True).encode("utf-8")
        return hashlib.sha256(snapshot_bytes).hexdigest()

    def run(self):
        print("[SWARM SYNC DAEMON] 🧠 Syncing swarm state...")
        while True:
            try:
                agents   = self._load_child_agents()
                snapshot = self._generate_swarm_snapshot(agents)

                if not isinstance(snapshot, dict):
                    print("[SWARM SYNC DAEMON] ⚠️ Malformed snapshot — expected dict")
                    time.sleep(self.interval)
                    continue

                snapshot_hash = self._hash_snapshot(snapshot)
                if snapshot_hash == self._last_snapshot_hash:
                    # No change — skip writing
                    time.sleep(self.interval)
                    continue

                # Additional guard: skip if all emotions are "unknown"
                if set(snapshot["emotional_distribution"].keys()) == {"unknown"}:
                    print("[SWARM SYNC DAEMON] ⚠️ All agent emotions unknown; skipping write.")
                    time.sleep(self.interval)
                    continue

                self._last_snapshot_hash = snapshot_hash

                with open(SWARM_FEED, "a") as f:
                    f.write(json.dumps(snapshot) + "\n")

                store_to_memory("swarm_feed", snapshot)
                print(f"[SWARM SYNC] ✅ Snapshot stored @ {snapshot['timestamp']}")
            except Exception as e:
                print(f"[SWARM SYNC ERROR] {e}")

            time.sleep(self.interval)