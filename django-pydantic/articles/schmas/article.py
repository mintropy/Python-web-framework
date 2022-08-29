import datetime

from pydantic import BaseModel, validator


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

    @validator("title")
    def title_length(cls, v):
        if len(v) > 20:
            return None
        return v
