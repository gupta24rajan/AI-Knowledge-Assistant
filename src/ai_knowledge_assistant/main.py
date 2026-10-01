from ai_knowledge_assistant.config import RAGConfig
from ai_knowledge_assistant.embeddings.sentence_transformer import SentenceTransformerEmbedding
from ai_knowledge_assistant.llm.groq_llm import GroqLLM
from ai_knowledge_assistant.rag.pipeline import RAGPipeline
from ai_knowledge_assistant.vectorstore.chroma_store import ChromaStore


config = RAGConfig()

embedding_model = SentenceTransformerEmbedding(
    model_name=config.embedding_model
)
vector_store = ChromaStore()
llm = GroqLLM(
     model_name=config.llm_model,
     api_key=config.groq_api_key
)

rag = RAGPipeline(
    embedding_model=embedding_model,
    vector_store=vector_store,
    llm=llm,
    config=config
)


question = "What are the function of Python?"


answer = rag.ask(question)


print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)


