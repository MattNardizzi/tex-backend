# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# License: Private Intellectual Property – Not for distribution.
# ============================================================
# ============================================
# Tex Vector Forge – Decision Embedding Engine
# ============================================

import hashlib
import datetime

class TexVectorForge:
    def __init__(self):
        self.vectors = []

    def embed(self, data):
        hash_input = str(data) + datetime.datetime.now().isoformat()
        vector_id = hashlib.sha256(hash_input.encode()).hexdigest()[:16]
        vector = {
            "id": vector_id,
            "data": data,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.vectors.append(vector)
        print(f"[VECTOR FORGE] 🔗 Embedded vector: {vector_id}")
        return vector
