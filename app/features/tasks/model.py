from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from app.db.base_model import BaseModel

class TasksModel(BaseModel):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('users.id'))
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
    prioridad = Column(String(10), nullable=False)
    completada = Column(Boolean, default=False, nullable=False)


    def __init__(self, id,id_usuario, nombre, descripcion, prioridad, completada) -> None:
        self.id = id
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = completada

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "prioridad": self.prioridad,
            "completada": self.completada
        }
