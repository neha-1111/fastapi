from sqlalchemy import Column, String, Integer, Boolean, text, TIMESTAMP,ForeignKey
from .database import base
from sqlalchemy.orm import relationship
class Post(base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default=text('true'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="cascade"),nullable=False)
    owner=relationship('user')
class user(base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)    
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
class vote(base):
    __tablename__="vote"
    user_id=Column(Integer,ForeignKey("users.id",ondelete="cascade"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="cascade"),primary_key=True)    

