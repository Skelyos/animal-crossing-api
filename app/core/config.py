from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
