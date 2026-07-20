from langchain_huggingface import HuggingFaceEmbeddings

from shared.config import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self):
        self.model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    def get(self):
        return self.model