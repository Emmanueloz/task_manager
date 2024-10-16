from app.db.base_model import BaseModel
from sqlalchemy import Column, String, Date, Integer
from datetime import date
from app import db

class Nota(BaseModel):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(String(1000), nullable=False)
    fecha_creacion = Column(Date, default=date.today, nullable=False)
    fecha_modificacion = Column(Date, default=date.today, onupdate=date.today, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
