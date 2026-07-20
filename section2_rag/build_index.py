from shared.config import (
    DOCUMENTS_DIR,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from section2_rag.loader import DocumentLoader
from section2_rag.chunker import DocumentChunker
from section2_rag.embeddings import EmbeddingModel
from section2_rag.vectorstore import VectorStore


loader = DocumentLoader(DOCUMENTS_DIR)

documents = loader.load()

print(f"Loaded {len(documents)} pages")

chunker = DocumentChunker(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

chunks = chunker.split(documents)

print(f"Created {len(chunks)} chunks")

embedding_model = EmbeddingModel().get()

db = VectorStore(embedding_model)

db.build(chunks)

print("FAISS index created successfully.")