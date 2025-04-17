from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str


class UserRead(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
