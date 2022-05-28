from sqlalchemy.orm import Session

from FastAPI import models, schemas


def get_article_list(db: Session):
    return db.query(models.Article).all()


def get_article(db: Session, article_id: int):
    return db.query(models.Article)\
        .filter(models.Article.id == article_id).first()


def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(
        title=article.title,
        content=article.content,
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
