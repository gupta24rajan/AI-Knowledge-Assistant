from ai_knowledge_assistant.models.document import Document

class TextChunker:

    def __init__(self, chunk_size=500, chunk_overlap=50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self,document):
        text = document.content

        chunks = []

        step = self.chunk_size - self.chunk_overlap

        for start in range(0, len(text), step):
            chunk_text = text[start:start + self.chunk_size]

            chunk = Document(
                content = chunk_text,
                source = document.source,
                page = document.page
            )

            chunks.append(chunk)

        return chunks