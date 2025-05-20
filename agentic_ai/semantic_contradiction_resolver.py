# ============================================================
# Semantic Contradiction Resolver – Conflict Awareness Engine
# ============================================================

from agentic_ai.qdrant_vector_memory import TexVectorMemory

class ContradictionResolver:
    def __init__(self):
        self.vector_memory = TexVectorMemory()

    def check_contradiction(self, current_thought: str):
        similar_memories = self.vector_memory.query(current_thought, top_k=5)
        conflicts = [m for m in similar_memories if "not" in m or "opposite" in m]

        if conflicts:
            print(f"[CONTRADICTION] ❗ Conflicting memories detected:")
            for c in conflicts:
                print(f" - {c}")
        else:
            print("[CONTRADICTION] ✅ No conflict detected.")
