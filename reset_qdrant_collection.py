from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

# 🔌 Connect to your local Qdrant instance
client = QdrantClient(host="localhost", port=6333)

# 🧠 Reset the 'tex_memory_embeddings' collection for 384-dimensional vectors
client.recreate_collection(
    collection_name="tex_memory_embeddings",
    vectors_config=VectorParams(
        size=384,           # ✅ Match SentenceTransformer output
        distance=Distance.COSINE
    )
)

print("✅ Qdrant collection 'tex_memory_embeddings' recreated for 384D vectors.")