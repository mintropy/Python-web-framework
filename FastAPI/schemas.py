from typing import List, Optional
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    
    class Config:
        orm_mode = True
