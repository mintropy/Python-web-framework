from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, column
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

    articles = relationship("Article", back_populates="user")
    replies = relationship("Article", back_populates="user")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    article_user_id = column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="articles")
    replies = relationship("Reply", back_populates="article")


class Reply(Base):
    __tablename__ = "replies"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    reply_user_id = column(Integer, ForeignKey("users.id"))
    reply_article_id = column(Integer, ForeignKey("articles.id"))

    user = relationship("User", back_populates="replies")
    article = relationship("Article", back_populates="replies")
