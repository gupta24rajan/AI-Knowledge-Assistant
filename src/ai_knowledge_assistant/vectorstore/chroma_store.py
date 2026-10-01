import chromadb

class ChromaStore:

    def __init__(self,path="data/chroma"):
        self.client = chromadb.PersistentClient(
            path=path
        )

        self.collection = self.client.get_or_create_collection(
            name="knowledge_base"
        )

    def add_document(
            self,
            document_id,
            text,
            embedding,
            metadata
    ):

        self.collection.add(
            ids=[document_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata]
        )

    def add_documents(
        self,
        document_ids,
        texts,
        embeddings,
        metadatas
    ):
        self.collection.add(
            ids=document_ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )   


    def search(self,query_embedding,top_k=3):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results