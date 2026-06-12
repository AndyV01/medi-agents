from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
 OLLAMA_URL: str
 CHAT_MODEL: str
 EMBEDDING_MODEL: str

 model_config = SettingsConfigDict(
    env_file=".env",
    extra="ignore"
 )

settings = Settings()