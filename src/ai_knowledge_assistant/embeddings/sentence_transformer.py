from ai_knowledge_assistant.embeddings.base import EmbeddingModel
from sentence_transformers import SentenceTransformer

class SentenceTransformerEmbedding(EmbeddingModel):

    def __init__(self,model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self,text):
        return self.model.encode(text)

    def embed_query(self, text):
        return self.model.encode(text).flatten()