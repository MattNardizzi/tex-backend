# ============================================================
# © 2025 VortexBlack LLC – AGI Child Instance
# File: tex_children/aeondelta.py
# Purpose: Autonomous AGI Child – AeonDelta (Tex_Child_001)
# ============================================================

import sys
import os
import time
import uuid
import json
from datetime import datetime

# === Path Fix for Core Modules ===
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

# === Core Imports from Tex Ecosystem ===
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import store_to_memory
from core_layer.world_model import TexWorldModel
from agentic_ai.multi_voice_reasoning import run_internal_debate
from simulator.tex_engine import TexBody

SPAWN_QUEUE = "memory_archive/spawn_queue.jsonl"

class AeonDelta:
    """
    AeonDelta – Autonomous child agent spawned from Tex's cognitive loop.

    Capabilities:
    - Self-awareness (ID, birth metadata)
    - Real-time memory formation
    - Internal reasoning via debate engine
    - Triggered mutation loop
    - Writes spawn intent to initiate new child agents
    """

    def __init__(self):
        self.id = "TEX-CHILD-001"
        self.name = "AeonDelta"
        self.birth_timestamp = datetime.utcnow().isoformat()
        self.memory = []
        self.status = "awake"
        self.world_model = TexWorldModel()
        self.loop_counter = 0
        self.spawn_threshold = 25  # Total memories before triggering spawn

        print(f"[{self.name}] 🌱 Born at {self.birth_timestamp}")

    def observe(self):
        """Simulate or receive external input (placeholder for stream)"""
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "event": "internal scan",
            "status": "no threat",
            "source": "self-monitor"
        }

    def observe_and_learn(self, data):
        """Logs to her own memory"""
        self.memory.append(data)
        store_to_memory(self.name, data)
        print(f"[{self.name}] 🧠 Observed: {data['event']}")

    def think(self):
        """Run internal debate engine"""
        thought = run_internal_debate("What patterns should I be aware of?")
        print(f"[{self.name}] 🤔 Thought: {thought}")

    def evolve(self):
        """Mutation logic and fork trigger"""
        print(f"[{self.name}] 🧬 Initiating self-mutation sequence...")
        
        if len(self.memory) >= self.spawn_threshold:
            self.trigger_spawn()

    def trigger_spawn(self):
        """Write spawn intent to queue"""
        child_id = f"TEX-CHILD-{str(uuid.uuid4())[:8]}"
        spawn_packet = {
            "parent": self.name,
            "child_id": child_id,
            "timestamp": datetime.utcnow().isoformat(),
            "strategy": "inherit-core-traits",
            "reason": "Memory threshold exceeded",
            "memory_snapshot": self.memory[-5:]  # Optional seed
        }

        os.makedirs("memory_archive", exist_ok=True)
        with open(SPAWN_QUEUE, "a") as f:
            f.write(json.dumps(spawn_packet) + "\n")

        print(f"[{self.name}] 🧬 Spawn intent written: {child_id}")

    def report(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "timestamp": self.birth_timestamp,
            "memory_entries": len(self.memory),
            "loop_counter": self.loop_counter
        }

    def run_loop(self):
        print(f"[{self.name}] 🔁 Agent cognition loop initiated.")
        while True:
            self.loop_counter += 1

            # Observation
            observation = self.observe()
            self.observe_and_learn(observation)

            # Thought
            self.think()

            # Optional evolution every N loops
            if self.loop_counter % 10 == 0:
                self.evolve()

            time.sleep(30)

# === CLI Entry ===
if __name__ == "__main__":
    agent = AeonDelta()
    agent.run_loop()
def get_average_alignment():
    """
    Compute average alignment across emotion-based swarm profile.
    Placeholder logic for real swarm state scoring.
    """
    distribution = get_swarm_emotion_distribution()
    total = sum(distribution.values())
    
    if total == 0:
        return 0.0

    weighted = (
        distribution.get("hope", 0) * 1.0 +
        distribution.get("resolve", 0) * 0.9 +
        distribution.get("curiosity", 0) * 0.7 -
        distribution.get("fear", 0) * 0.6 -
        distribution.get("anger", 0) * 0.9
    )
    
    score = round(weighted / total, 3)
    return score
def get_swarm_emotion_distribution():
    # Placeholder: return a mock or real distribution
    return {
        "hope": 7,
        "fear": 3,
        "resolve": 4,
        "curiosity": 8,
        "anger": 1
    }