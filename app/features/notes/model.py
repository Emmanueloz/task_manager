from app.db.base_model import BaseModel
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime


class Nota(BaseModel):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(String(1000), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow, nullable=False)
    fecha_modificacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
