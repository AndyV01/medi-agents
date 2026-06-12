from langchain_ollama import ChatOllama
from app.core.config import settings

llm = ChatOllama(
    model=settings.CHAT_MODEL,
    base_url=settings.OLLAMA_URL,
    temperature=0
)