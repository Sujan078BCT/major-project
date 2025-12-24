from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # App Configuration
    project_name: str = "FastAPI Project"
    version: str = "1.0.0"
    description: str = "A FastAPI project"
    debug: bool = True
    
    # Server Configuration
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True
    
    # CORS Configuration
    cors_origins: List[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["*"]
    cors_allow_headers: List[str] = ["*"]
    
    # Database Configuration
    database_url: str = "sqlite:///./db/fastapi_project.db"
    database_echo: bool = False
    
    # Authentication Configuration
    secret_key: str = "your-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    model_config = {"env_file": ".env"}

settings = Settings() 