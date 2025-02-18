from pydantic_settings import BaseSettings
import os
from pathlib import Path
from typing import List, Optional, Union
from pydantic import validator

class Settings(BaseSettings):
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Stock Analysis API"
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    
    # OpenAI Configuration
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    
    # Static folder for plots
    STATIC_DIR: Path = Path(__file__).parent.parent / "static"
    PLOT_FOLDER: Path = STATIC_DIR / "plots"
    
    # Environment
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    @validator("OPENAI_API_KEY", pre=True)
    def validate_openai_key(cls, v: Optional[str]) -> str:
        if not v or v == "your-openai-api-key-here":
            raise ValueError("OPENAI_API_KEY must be set in environment")
        return v
    
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create instance of settings
settings = Settings()

# Ensure directories exist
settings.STATIC_DIR.mkdir(exist_ok=True)
settings.PLOT_FOLDER.mkdir(exist_ok=True) 