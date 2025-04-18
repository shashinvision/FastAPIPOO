from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)


class UserCreate(BaseModel):
    username: str
    email: str


class UserRead(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
