from app.db.base_model import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)
