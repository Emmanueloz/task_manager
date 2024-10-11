from app.db.sql import db
from app.features.tasks.model import TasksModel
from sqlalchemy import or_
from sqlalchemy.orm import joinedload


def add_campus(
        nombre: str,
        descripcion: text,
        prioridad: str,
        completada: Boolean,
):
    try:
        if TasksModel.query.filter(TasksModel.nombre == nombre, TasksModel.estado == 1).first():
            return None, "El campus ya existe"

        if nombre == "" and descripcion == "" and prioridad == "" and completada == "":
            return None, "Todos los campos son obligatorios"

        tasks = TasksModel(
            nombre, descripcion, prioridad, completada)

        db.session.add(tasks)
        db.session.commit()
        return tasks.id, None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al guardar el campus: {e}"

