from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routes import items, villagers

app = FastAPI(title=settings.PROJECT_NAME)

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "http://localhost:8100",
    "https://churchofiron.co.uk",
    "https://www.churchofiron.co.uk",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, tags=["items"], prefix="/items")
app.include_router(villagers.router, tags=["villagers"], prefix="/villagers")

handler = Mangum(app)
