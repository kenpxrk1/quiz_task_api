from fastapi import FastAPI
from api import router

app = FastAPI(
    title="QUIZ-API"
)

app.include_router(router)

