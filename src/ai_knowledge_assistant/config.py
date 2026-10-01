from pydantic_settings import BaseSettings, SettingsConfigDict


class RAGConfig(BaseSettings):

    groq_api_key: str

    llm_model: str = "openai/gpt-oss-20b"

    embedding_model: str = "all-MiniLM-L6-v2"

    chunk_size: int = 500

    chunk_overlap: int = 50

    top_k: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )



    # ----- This is the Manual configuragtion ---------  
# import os
# from dataclasses import dataclass

# from dotenv import load_dotenv


# load_dotenv()

# @dataclass
# class RAGConfig:

#     chunk_size: int = int(
#          os.getenv("CHUNK_SIZE", "500")
#     )

#     chunk_overlap: int = int(
#         os.getenv("CHUNK_OVERLAP", "50")
#     ) 

#     top_k: int = int(
#         os.getenv("TOP_K", "3")
#     )

#     embedding_model: str = "all-MiniLM-L6-v2"

#     llm_model: str = os.getenv(
#          "LLM_MODEL",
#         "openai/gpt-oss-20b"
#     )

