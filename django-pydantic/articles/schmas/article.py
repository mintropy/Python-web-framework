from xml.etree.ElementInclude import include
from djantic import ModelSchema

from ..models import Article


class ArticleListSchema(ModelSchema):
    reply_count: int = 0

    class Config:
        model = Article
        include = ('id', 'title', 'created_at', 'reply_count')
