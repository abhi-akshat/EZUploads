from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str


class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String) 
    user_type = Column(String)
    
class File(Base):
    __tablename__ = "files"
    
    id = Column(String, primary_key=True, index=True)
    filename = Column(String, unique=True, index=True)
    link = Column(String)