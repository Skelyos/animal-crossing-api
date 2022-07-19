from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    MONGODB_USER: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str

    # return f"mongodb+srv://{values.get('MONGODB_USER')}:{values.get('MONGODB_PASSWORD')}@{values.get('MONGODB_DATABASE')}/?retryWrites=true&w=majority"

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
