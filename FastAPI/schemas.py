from datetime import datetime

from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    # article_user_id: int

    class Config:
        orm_mode = True


class ReplyBase(BaseModel):
    content: str
    created_at: datetime
    updated_at: datetime
    # reply_user_id: int
    # reply_article_id: int

    class Config:
        orm_mode = True
