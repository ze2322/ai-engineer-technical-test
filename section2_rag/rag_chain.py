from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate

from shared.config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TOP_K,
)

from section2_rag.embeddings import EmbeddingModel
from section2_rag.vectorstore import VectorStore


class RAGPipeline:

    def __init__(self):

        embeddings = EmbeddingModel().get()

        self.db = VectorStore(embeddings).load()

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say exactly:

"I couldn't find relevant information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
        )

    def ask(self, question):

        docs = self.db.similarity_search(question, k=TOP_K)

        if len(docs) == 0:
            return "I couldn't find relevant information in the provided documents."

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        chain = self.prompt | self.llm

        response = chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        sources = []

        for doc in docs:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", 0)

            sources.append(f"{source} (page {page+1})")

        return {
            "answer": response.content,
            "sources": list(set(sources)),
        }