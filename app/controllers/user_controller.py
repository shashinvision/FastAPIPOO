from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user_model import UserRead, UserCreate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])
user_service = UserService()


@router.get("/", response_model=List[UserRead])
def read_users():
    return user_service.get_users()


@router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserRead)
def create_user(user: UserCreate):
    return user_service.create_user(user.username, user.email)
