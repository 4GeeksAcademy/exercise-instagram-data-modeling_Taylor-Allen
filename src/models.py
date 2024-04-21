import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    photo_or_video = Column(String(250), nullable=False)
    description = Column(String(250))
    likes = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    likes = Column(Integer, default=0)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    create_date = Column(Date, default=date.today(), nullable=False)
    sender_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    sender = relationship(User)
    rep_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    rep = relationship(User)

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    photo_or_video = Column(String(250), nullable=False)
    description = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e