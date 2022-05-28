# from dataclasses import dataclass
from pydantic.dataclasses import dataclass
from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from FastAPI.database import Base


class Article(Base):
    __tablename__ = "articles"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

