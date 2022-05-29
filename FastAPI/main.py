from fastapi import FastAPI

from FastAPI.routers import articles


app = FastAPI()

app.include_router(articles.router, prefix="/articles")
