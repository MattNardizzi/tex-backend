# test_qdrant_connection.py
import os
import time
from qdrant_client import QdrantClient

def _init_client():
    host = os.getenv("TEX_VECTOR_HOST", "localhost")
    port = int(os.getenv("TEX_VECTOR_PORT", "6333"))

    for attempt in range(10):
        try:
            print(f"[QDRANT] Connecting to {host}:{port} (Attempt {attempt+1}/10)")
            client = QdrantClient(host=host, port=port)
            print("✅ Qdrant connection successful!")
            return client
        except Exception as e:
            print(f"❌ Connection failed, retrying in 2s: {e}")
            time.sleep(2)

    raise ConnectionError("[QDRANT] ❌ Unable to connect after max retries")

# Run the test
_init_client()