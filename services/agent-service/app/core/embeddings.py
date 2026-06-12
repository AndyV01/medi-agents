from langchain_ollama import OllamaEmbeddings
from app.core.config import settings

embeddings = OllamaEmbeddings(
    model=settings.EMBEDDING_MODEL,
    base_url=settings.OLLAMA_URL
)