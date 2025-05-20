# ===========================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC – All rights reserved
# File: agentic_ai/vectorize_reasoning.py
#
# Purpose
# -------
#  • Batch-index the reasoning-trace archive into Qdrant
#  • Provide a helper to stream fresh reasoning vectors in real time
#
# Design changes
# --------------
# 1. **NO raw QdrantClient here** – everything goes through
#    `agentic_ai.qdrant_vector_memory`, which:
#        • waits for Qdrant to be ready
#        • retries on failure
#        • guarantees the collection exists
# 2. Model / paths are configurable via env-vars.
# ===========================================================

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any

from sentence_transformers import SentenceTransformer

from agentic_ai.qdrant_vector_memory import (
    upsert_embeddings,
    _ensure_collection,          # re-use the idempotent bootstrap
)

# ---------------------------------------------------------------------
# 🛠 Configuration – tweak by exporting env-vars before launch
# ---------------------------------------------------------------------
LOG_PATH      = Path(os.getenv("TEX_TRACE_LOG", "memory_archive/reasoning_trace_log.jsonl"))
COLLECTION    = os.getenv("TEX_REASONING_COLLECTION", "tex_reasoning_memory")
EMBED_MODEL   = os.getenv("TEX_EMBEDDING_MODEL", "all-MiniLM-L6-v2")

# ---------------------------------------------------------------------
# 🔣 Embedding model
# ---------------------------------------------------------------------
embedder = SentenceTransformer(EMBED_MODEL)
VECTOR_DIM = embedder.get_sentence_embedding_dimension()

# ---------------------------------------------------------------------
# 🚀 Batch indexing
# ---------------------------------------------------------------------
def _load_trace_lines() -> List[Dict[str, Any]]:
    if not LOG_PATH.exists():
        print(f"[⚠️] No trace log found at {LOG_PATH}")
        return []
    with LOG_PATH.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def _vec(text: str) -> List[float]:
    return embedder.encode(text, normalize_embeddings=True).tolist()


def batch_index() -> None:
    _ensure_collection()                     # idempotent
    lines = _load_trace_lines()
    if not lines:
        return

    ids, vecs, payloads = [], [], []
    for trace in lines:
        text = (trace.get("output") or trace.get("input") or "").strip()
        if not text:
            continue

        ids.append(trace.get("id") or len(ids))     # fallback id
        vecs.append(_vec(text))
        payloads.append(trace)

    if ids:
        upsert_embeddings(ids, vecs, payloads)
        print(f"[🧠] Indexed {len(ids)} reasoning traces → Qdrant")
    else:
        print("[🟡] Nothing to index – no text payloads found")


# ---------------------------------------------------------------------
# ✍️ Real-time helper
# ---------------------------------------------------------------------
def store_reasoning(text: str) -> None:
    """
    Vectorise `text` and push it to Qdrant immediately.
    Call this from your live pipeline (e.g. inside tex_core).
    """
    _ensure_collection()

    vec = _vec(text)
    now = datetime.now(timezone.utc)
    upsert_embeddings(
        ids      = [int(now.timestamp() * 1000)],     # millisecond epoch
        vectors  = [vec],
        payloads = [{
            "output": text,
            "timestamp": now.isoformat(timespec="seconds")
        }],
    )
    print("[VECTOR STORAGE] 🧠 Stored live reasoning vector → Qdrant")


# ---------------------------------------------------------------------
# 🔹 CLI usage ---------------------------------------------------------
# ---------------------------------------------------------------------
if __name__ == "__main__":
    batch_index()