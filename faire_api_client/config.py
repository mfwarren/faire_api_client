from pydantic import BaseSettings

class Settings(BaseSettings):
    api_version: str = 'v2'
    base_url: str = 'https://www.faire.com/external-api'

settings = Settings()  # Ensure to call the settings instance
