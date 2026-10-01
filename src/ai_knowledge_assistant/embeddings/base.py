from abc import ABC, abstractmethod

class EmbeddingModel(ABC):

    @abstractmethod
    def embed_documents(self,text):
        pass

    @abstractmethod
    def embed_query(self, text):
        pass