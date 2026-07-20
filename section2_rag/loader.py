from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:
    def __init__(self, documents_dir: Path):
        self.documents_dir = documents_dir

    def load(self):
        documents = []

        pdf_files = list(self.documents_dir.glob("*.pdf"))

        if not pdf_files:
            raise FileNotFoundError(
                f"No PDF files found in {self.documents_dir}"
            )

        for pdf in pdf_files:
            loader = PyPDFLoader(str(pdf))
            documents.extend(loader.load())

        return documents