from pymongo import MongoClient

from app.core.config import settings

mongodb_uri = f"mongodb+srv://{settings.MONGODB_USER}:{settings.MONGODB_PASSWORD}@{settings.MONGODB_DATABASE}/?retryWrites=true&w=majority"
mongodb_client = MongoClient(mongodb_uri)

# Stating database connection
database_name = "animal-crossing"
mongo_database = mongodb_client[database_name]
