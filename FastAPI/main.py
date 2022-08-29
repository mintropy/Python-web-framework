from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/articles/", response_model=List[schemas.ArticleBase])
def read_articles(db: Session = Depends(get_db)):
    return crud.get_articles(db)


@app.get("/articles/{article_id}/", response_model=schemas.ArticleBase)
def read_article_detail(article_id: int, db: Session = Depends(get_db)):
    return crud.get_article_detail(db=db, article_id=article_id)


app = FastAPI()


@app.post("/articles/", response_model=schemas.ArticleBase)
def create_article(article: schemas.ArticleBase, db: Session = Depends(get_db)):
    return crud.create_articles(db=db, article=article)
