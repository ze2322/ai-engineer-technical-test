from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = PROJECT_ROOT / "section2_rag" / "documents"

VECTOR_DB_DIR = PROJECT_ROOT / "section2_rag" / "vector_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "llama3.2"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 4

OLLAMA_MODEL = "llama3.2"
OLLAMA_BASE_URL = "http://localhost:11434"