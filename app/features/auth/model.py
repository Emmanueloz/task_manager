from app.db.base_model import BaseModel
from sqlalchemy import Column, String

from flask_login import UserMixin


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)


class UserLogin(UserMixin):
    def __init__(self, user: User):
        self.id = user.id
        self.username = user.username
        self.email = user.email
