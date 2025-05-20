# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: future_layer/multiworld_memory.py
# Tier 5: Tex AGI — Multi-World Strategic Memory Engine
# ============================================================

import uuid
from datetime import datetime
from core_layer.tex_manifest import TEXPULSE
from core_layer.memory_engine import recall_all  # ✅ Added for recall_fused_insights

# === Mock Qdrant storage system (replace with production vector store)
class MockVectorStore:
    def __init__(self):
        self.storage = {}

    def upsert(self, collection_name, vector_id, vector_payload):
        self.storage[vector_id] = {"collection": collection_name, "payload": vector_payload}

qdrant_client = MockVectorStore()

class MultiWorldMemory:
    def __init__(self):
        self.collection = "multiworld_universes"

    def store_world(self, world_state):
        """AGI-fused universe archival logic — embeds cognitive context."""
        vector_id = str(uuid.uuid4())
        emotion = TEXPULSE.get("emotional_state", "curious")
        urgency = TEXPULSE.get("urgency", 0.7)
        coherence = TEXPULSE.get("coherence", 0.8)

        divergence_score = world_state.get("divergence_score", 0.0)
        chaos_flag = self._is_chaotic(world_state)
        entropy_signature = self._generate_entropy_signature(emotion, urgency, coherence)

        payload = {
            "vector_id": vector_id,
            "timestamp": datetime.utcnow().isoformat(),
            "emotion_context": emotion,
            "urgency_context": urgency,
            "coherence_context": coherence,
            "entropy_signature": entropy_signature,
            "divergence_score": divergence_score,
            "chaos_detected": chaos_flag,
            "world_state": world_state
        }

        qdrant_client.upsert(self.collection, vector_id, payload)
        print(f"[MULTIWORLD MEMORY] 🧠 Stored universe: {vector_id} | Divergence={divergence_score} | Chaos={chaos_flag}")

    def store_multiple_worlds(self, world_list):
        """Store multiple universe simulations with cognitive imprint."""
        for world in world_list:
            self.store_world(world)

    def recall_fused_insights(self):
        """Retrieve previously stored multiworld fused threads."""
        try:
            memories = recall_all("multiworld_fused_memory")
            return [m["thread"] for m in memories if "thread" in m]
        except Exception as e:
            print(f"[MULTIWORLD MEMORY ERROR] Failed to recall fused insights: {e}")
            return []

    def _is_chaotic(self, world):
        """Detects timeline instability via mutation and low coherence."""
        events = world.get("events", [])
        mutation_count = sum(1 for e in events if e.get("mutation_triggered", False))
        avg_coherence = sum(e.get("coherence", 0.7) for e in events) / max(1, len(events))
        return mutation_count >= 2 or avg_coherence < 0.5

    def _generate_entropy_signature(self, emotion, urgency, coherence):
        """Create a compact vector fingerprint for AGI traceability."""
        return f"E:{emotion[:2].upper()}|U:{int(urgency * 100)}|C:{int(coherence * 100)}"

# === Usage
if __name__ == "__main__":
    memory = MultiWorldMemory()
    sample_universes = [
        {
            "divergence_score": 0.68,
            "events": [
                {"coherence": 0.44, "mutation_triggered": True},
                {"coherence": 0.48, "mutation_triggered": True}
            ]
        },
        {
            "divergence_score": 0.22,
            "events": [
                {"coherence": 0.82, "mutation_triggered": False},
                {"coherence": 0.86, "mutation_triggered": False}
            ]
        }
    ]
    memory.store_multiple_worlds(sample_universes)