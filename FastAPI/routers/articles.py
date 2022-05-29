from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from FastAPI import models, schemas, crud, database


router = APIRouter()


@router.get("/", response_model=List[schemas.Article])
def article_list(db: Session = Depends(database.get_db)):
    articles = crud.get_article_list(db)
    return {}


@router.post("/", response_model=schemas.Article)
def article_create(article: schemas.Article, db: Session = Depends(database.get_db)):
    return crud.create_article(db=db, article=article)
