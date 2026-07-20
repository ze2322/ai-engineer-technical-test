from langchain_community.vectorstores import FAISS

from shared.config import VECTOR_DB_DIR


class VectorStore:

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def build(self, chunks):

        db = FAISS.from_documents(
            chunks,
            self.embeddings,
        )

        db.save_local(str(VECTOR_DB_DIR))

        return db

    def load(self):

        return FAISS.load_local(
            str(VECTOR_DB_DIR),
            self.embeddings,
            allow_dangerous_deserialization=True,
        )