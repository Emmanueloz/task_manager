from sqlalchemy import Column, Integer, String, Enum, Boolean
from app.db.base_model import BaseModel
import enum

# Enum para la prioridad
class TaskPriority(enum.Enum):
    baja = "Baja"
    media = "Media"
    alta = "Alta"

class TasksModel(BaseModel):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
    prioridad = Column(Enum(TaskPriority), nullable=False) 
    completada = Column(Boolean, default=False, nullable=False)
