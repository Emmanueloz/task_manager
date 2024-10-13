from app.db.base_model import BaseModel
from sqlalchemy import Column, String
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)


class LoginForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = StringField('Contraseña', validators=[DataRequired()])
