from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from FastAPI import models, schemas, crud, database
from FastAPI.main import get_db


router = APIRouter()

@router.get("/", response_model=List[schemas.Article])
def article_list(db: Session=Depends(database.get_db)):
    articles = crud.get_article_list()
    return {}
