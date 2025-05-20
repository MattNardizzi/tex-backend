# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: core_layer/TimeForkRepeater.py
# Purpose: Simulates the same event loop under divergent codex, emotion, and goal overlays.
# ============================================================

import json
import random
from datetime import datetime
from core_layer.memory_engine import store_to_memory

FORK_LOOP_LOG = "memory_archive/time_fork_repeats.jsonl"

class TimeForkRepeater:
    def __init__(self):
        self.variants = []

    def loop_event(self, base_event, iterations=5):
        print(f"[TIMEFORK] ⏳ Repeating event: '{base_event['event']}' for {iterations} forks...")

        for i in range(iterations):
            fork = self._mutate(base_event, i)
            self.variants.append(fork)
            store_to_memory("time_fork_repeat", fork)
            self._log_fork(fork)

        return self.variants

    def _mutate(self, event, index):
        emotions = ["resolve", "curiosity", "doubt", "ambition", "fear"]
        codex_versions = ["E-Prime v1.2", "AEI-Loop3", "RedLine-5", "PhantomRoot"]
        priorities = ["profit", "ethics", "coherence", "exploration"]

        fork = {
            "fork_id": f"FORK_LOOP_{index}",
            "timestamp": datetime.utcnow().isoformat(),
            "event": event["event"],
            "emotion": random.choice(emotions),
            "codex_version": random.choice(codex_versions),
            "priority": random.choice(priorities),
            "context": event.get("context", {})
        }
        return fork

    def _log_fork(self, fork):
        with open(FORK_LOOP_LOG, "a") as f:
            f.write(json.dumps(fork) + "\n")
        print(f"[TIMEFORK] 🌐 Fork created: {fork['fork_id']} | Emotion={fork['emotion']} | Codex={fork['codex_version']}")


if __name__ == "__main__":
    repeater = TimeForkRepeater()
    test_event = {
        "event": "strategic_alpha_response",
        "context": {"ticker": "NVDA", "signal": "momentum_surge"}
    }
    repeater.loop_event(test_event, iterations=5)