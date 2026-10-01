class RAGPipeline:

    def __init__(
        self,
        embedding_model,
        vector_store,
        llm,
        config
    ):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.llm = llm
        self.config = config


    def ask(self,question):


        #step1: Convert question into embeddig
        query_vector = self.embedding_model.embed_query(
            question
        )

        #step2: Search relevant chunks
        results = self.vector_store.search(
            query_embedding=query_vector.tolist(),
            top_k=self.config.top_k
        )

        #step3: Extract retrieved documents
        documents = results["documents"][0]

        # Step 4: Combine documents into context
        context = "\n\n".join(documents)

        # Step 5: Create prompt
        prompt = f"""
You are a helpful AI assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

If the answer is not present in the context,
say that you don't know based on the provided documents.
"""
        # Step 6: Send prompt to LLM
        answer = self.llm.generate(prompt)

        return answer
