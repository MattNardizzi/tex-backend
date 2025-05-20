from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)

# Test create collection
client.recreate_collection(
    collection_name="tex_test_collection",
    vectors_config={"size": 384, "distance": "Cosine"}
)
print("✅ Qdrant connection confirmed.")