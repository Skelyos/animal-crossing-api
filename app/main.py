from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME)

    origins = [
        "http://localhost",
        "https://localhost",
        "http://localhost:8080",
        "http://localhost:8100",
        f"https://{settings.env}.blox.oceidon.com",
        f"https://www.{settings.env}.blox.oceidon.com",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = get_application()
