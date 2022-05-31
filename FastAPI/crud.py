from sqlalchemy.orm import Session

from . import models, schemas


def get_articles(db: Session):
    return db.query(models.Article).all()


def get_article_detail(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()


def create_articles(db: Session, article: schemas.ArticleBase):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
