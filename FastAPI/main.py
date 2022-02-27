"""Fast API main"""
from typing import Optional

from fastapi import FastAPI

from .articles import router

app = FastAPI()

app.include_router(
    router.article_router
)


@app.get('/')
def read_root():
    return {'Hello': 'World'}
