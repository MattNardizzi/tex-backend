# ============================================================
# Tex Vector Bridge – Awareness to Memory Sync
# ============================================================

from agentic_ai.qdrant_vector_memory import TexVectorMemory

class VectorBridge:
    def __init__(self):
        self.memory = TexVectorMemory()

    def store_awareness(self, summary: dict):
        thought = f"Cycle thought: Emotion={summary['emotion']}, Urgency={summary['urgency']}, Coherence={summary['coherence']}"
        self.memory.embed_memory(thought, metadata={"type": "cycle_summary"})

    def recall_similar(self, query: str):
        return self.memory.query(query)
