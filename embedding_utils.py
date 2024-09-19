# embedding_utils.py

from sentence_transformers import SentenceTransformer

def initialize_embedding_model(model_name='all-MiniLM-L6-v2'):
    print("Initializing the Sentence Transformer model...")
    model = SentenceTransformer(model_name)
    print("Sentence Transformer model initialized.")
    return model

def generate_embeddings(embedding_model, text_dict):
    print("Generating embeddings for each section...")
    embeddings = {}
    for section, text in text_dict.items():
        print(f"Generating embedding for {section}...")
        section_embedding = embedding_model.encode(text)
        embeddings[section] = section_embedding
    print("Embedding generation completed.")
    return embeddings
