# ============================================================
# © 2025 Matthew Nardizzi / VortexBlack LLC. All rights reserved.
# File: agentic_ai/qdrant_vector_memory.py
# Purpose: Robust, container + cloud-friendly Qdrant helper
# ============================================================

"""Qdrant connection layer for Tex memory vector store.

Key design features:
- Container-aware host resolution (Docker, Compose, or Cloud)
- Configurable retry & backoff logic
- Idempotent collection creation
- Minimal and safe public API
"""

from __future__ import annotations

import os
import time
from typing import Any, Dict, List, Optional

from qdrant_client import QdrantClient
from qdrant_client.http import models as qdrant
from qdrant_client.http.exceptions import UnexpectedResponse


# -----------------------------------------------------------------------------
# 🔧 Config (env overrideable)
# -----------------------------------------------------------------------------
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant") # use Qdrant Cloud or Docker host
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_TIMEOUT = float(os.getenv("QDRANT_TIMEOUT", "10.0"))

RETRY_DELAY = float(os.getenv("QDRANT_RETRY_DELAY", "3"))  # base delay in seconds
MAX_RETRIES = int(os.getenv("QDRANT_MAX_RETRIES", "10"))

COLLECTION = os.getenv("QDRANT_COLLECTION", "tex_memory_embeddings")
VECTOR_SIZE_RAW = os.getenv("QDRANT_VECTOR_SIZE", "384")
DISTANCE = qdrant.Distance.COSINE

try:
    VECTOR_SIZE = int(VECTOR_SIZE_RAW)
    assert VECTOR_SIZE > 0
except Exception:
    raise ValueError(f"Invalid VECTOR_SIZE: {VECTOR_SIZE_RAW}")


# -----------------------------------------------------------------------------
# 🔁 Resilient connection bootstrap
# -----------------------------------------------------------------------------
def _init_client() -> QdrantClient:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if ":" in QDRANT_HOST:
                qdrant_url = f"http://{QDRANT_HOST}"
            else:
                qdrant_url = f"http://{QDRANT_HOST}:{QDRANT_PORT}"

            client = QdrantClient(url=qdrant_url, timeout=QDRANT_TIMEOUT)
            client.get_collections()
            print(f"[QDRANT] ✅ Connected to {qdrant_url}")
            return client

        except Exception as exc:
            print(f"[QDRANT] ⚠️  Connection failed ({exc}) – retry {attempt}/{MAX_RETRIES}")
            if attempt == MAX_RETRIES:
                raise ConnectionError("[QDRANT] ❌ Unable to connect after max retries") from exc
            time.sleep(RETRY_DELAY * attempt)  # exponential backoff

_client: QdrantClient = _init_client()


# -----------------------------------------------------------------------------
# 🚀 Safe, idempotent collection creation
# -----------------------------------------------------------------------------
def _ensure_collection() -> None:
    try:
        print(f"[QDRANT] 🌀 Ensuring collection '{COLLECTION}' exists...")
        _client.create_collection(
            collection_name=COLLECTION,
            vectors_config=qdrant.VectorParams(
                size=VECTOR_SIZE,
                distance=DISTANCE,
            ),
        )
        print(f"[QDRANT] ✅ Collection '{COLLECTION}' created successfully.")
    except qdrant.exceptions.UnexpectedResponse as e:
        if "already exists" in str(e):
            print(f"[QDRANT] 📚 Collection '{COLLECTION}' already exists — skipping creation.")
        else:
            print(f"[QDRANT] ❌ Unexpected error: {e}")
            raise e


# -----------------------------------------------------------------------------
# ✍️ Public API
# -----------------------------------------------------------------------------
def upsert_embeddings(
    ids: List[str],
    vectors: List[List[float]],
    payloads: Optional[List[Dict[str, Any]]] = None,
) -> None:
    """Insert or update vector embeddings in Qdrant."""
    try:
        _client.upsert(
            collection_name=COLLECTION,
            points=qdrant.Batch(ids=ids, vectors=vectors, payloads=payloads),
            wait=True,
        )
    except Exception as exc:
        print(f"[QDRANT] ❌ Upsert error – {exc}")


def query_similar(
    vector: List[float],
    top_k: int = 5,
    with_payload: bool = True,
) -> List[qdrant.ScoredPoint]:
    """Return top_k nearest vectors from Qdrant."""
    try:
        return _client.search(
            collection_name=COLLECTION,
            query_vector=vector,
            limit=top_k,
            with_payload=with_payload,
        )
    except UnexpectedResponse as exc:
        print(f"[QDRANT] ❌ Search error – {exc}")
        return []


def is_alive() -> bool:
    """Returns True if Qdrant collection is available."""
    try:
        _client.get_collection(COLLECTION)
        return True
    except Exception:
        return False
