import datetime

from djantic import ModelSchema
from pydantic import BaseModel

from ..models import Article


class ArticleListSchema(BaseModel):
    id: int
    title: str
    created_at: datetime.datetime
    replies_count: int


class ArticleDetailSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

