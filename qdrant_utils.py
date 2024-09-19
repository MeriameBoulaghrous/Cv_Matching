# qdrant_utils.py

import uuid
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

def initialize_qdrant_client(host="http://localhost:6333"):
    return QdrantClient(host)

def create_qdrant_collection(qdrant_client, collection_name, embedding_size):
    if not qdrant_client.collection_exists(collection_name=collection_name):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=embedding_size, distance=Distance.COSINE)
        )

def store_embeddings_in_qdrant(qdrant_client, embeddings, doc_id, collection_name="cv_embeddings"):
    for section, embedding in embeddings.items():
        point_id = str(uuid.uuid4())  # Generate a UUID for the point ID
        
        qdrant_client.upsert(
            collection_name=collection_name,
            points=[
                {
                    "id": point_id,
                    "vector": embedding.tolist(),  # Convert numpy array to list
                    "payload": {"section": section, "doc_id": doc_id}
                }
            ]
        )
    print(f"Embeddings for document {doc_id} have been stored in Qdrant.")
