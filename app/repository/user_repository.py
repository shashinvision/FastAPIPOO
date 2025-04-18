from app.models.entities.user_entity import User
from app.db.database import SessionLocal

# Repository functions using SessionLocal directly


def get_all_users():
    with SessionLocal() as db:
        return db.query(User).all()


def get_user_by_id(user_id: int):
    with SessionLocal() as db:
        return db.query(User).filter(User.id == user_id).first()


def create_user(username: str, email: str):
    with SessionLocal() as db:
        db_user = User(username=username, email=email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
