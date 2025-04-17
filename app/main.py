from fastapi import FastAPI
from app.db.database import engine, Base
from app.controllers import user_controller

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router)
