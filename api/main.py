from fastapi import FastAPI
from api.api import router

app = FastAPI(
    title="QUIZ-API"
)

app.include_router(router)

