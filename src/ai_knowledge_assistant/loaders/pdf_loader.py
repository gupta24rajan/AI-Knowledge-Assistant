from ai_knowledge_assistant.loaders.base import DocumentLoader
from ai_knowledge_assistant.models.document import Document
from ai_knowledge_assistant.paths import resolve_path
import pymupdf
import re
import unicodedata
from pathlib import Path

PUA_PATTERN = re.compile(r"[\ue000-\uf8ff]")


def normalize_text(text):
    text = unicodedata.normalize("NFKC", text)
    return PUA_PATTERN.sub(" ", text)


class PDFLoader(DocumentLoader):

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):

        file_path = resolve_path(self.file_path)

        pdf = pymupdf.open(file_path)

        documents = []

        for page_number, page in enumerate(pdf):

            text = page.get_text()

            document = Document(
                content=text,
                source=self.file_path,
                page=page_number + 1
            )

            documents.append(document)

        pdf.close()

        return documents