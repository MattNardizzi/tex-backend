# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/query_reasoning.py
#
# Purpose
# --------
# Retrieve semantically-similar reasoning traces from Qdrant **without**
# ever creating a raw `QdrantClient` here.  All connectivity & retries
# are delegated to the shared helper `qdrant_vector_memory.py`.
# ===========================================================

from __future__ import annotations

from typing import List, Dict, Any
import os

from sentence_transformers import SentenceTransformer

# Centralised, retry-hardened helper -------------------------
from agentic_ai.qdrant_vector_memory import query_similar

# -----------------------------------------------------------
# 🛠 Config (via env so you can switch models without editing)
# -----------------------------------------------------------
MODEL_NAME = os.getenv("TEX_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
COLLECTION  = os.getenv("TEX_REASONING_COLLECTION", "tex_reasoning_memory")
TOP_K       = int(os.getenv("TEX_REASONING_TOP_K", "3"))

model = SentenceTransformer(MODEL_NAME)


def _encode(text: str) -> List[float]:
    """Return a list[float] embedding for `text`."""
    return model.encode(text, normalize_embeddings=True).tolist()


def pretty_print(hits: List[Any], query: str) -> None:
    print(f"\n🔍 Query: «{query}»")
    if not hits:
        print("  (no matches)")
        return

    print("🧠 Most similar reasoning traces:\n")
    for h in hits:
        ts   = h.payload.get("timestamp", "unknown-time")
        out  = h.payload.get("output", "(no-text)").strip()
        conf = h.payload.get("confidence", "-")
        agent = h.payload.get("agent", "-")

        print(f" • [{ts}] {out}")
        print(f"   ↳ confidence={conf}  agent={agent}  score={h.score:.4f}\n")


def query_reasoning_memory(text: str, top_k: int = TOP_K) -> None:
    vec  = _encode(text)
    hits = query_similar(vec, top_k=top_k, with_payload=True)
    pretty_print(hits, text)


# ------------------------------------------------------------------
# 🔹 CLI usage ------------------------------------------------------
# ------------------------------------------------------------------
if __name__ == "__main__":
    import sys

    query = " ".join(sys.argv[1:]) or "What did Tex say about market volatility?"
    query_reasoning_memory(query)