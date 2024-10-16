from app.db.base_model import BaseModel
from sqlalchemy import Column, String, DateTime, Integer
from datetime import datetime
from app import db

class Nota(BaseModel):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(String(1000), nullable=False)
    fecha_creacion = Column(DateTime, default=lambda: datetime.now().replace(second=0, microsecond=0), nullable=False)
    fecha_modificacion = Column(DateTime, default=lambda: datetime.now().replace(second=0, microsecond=0), onupdate=lambda: datetime.now().replace(second=0, microsecond=0), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
