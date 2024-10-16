from app.db.db import db
from app.features.tasks.model import TasksModel
from sqlalchemy import or_

class FiltrosTareas:
    NOMBRE = "nombre"
    DESCRIPCION = "descripcion"
    PRIORIDAD = "prioridad"
    COMPLETADA = "completada"

    @classmethod
    def get_filter(cls):
        return [cls.NOMBRE, cls.DESCRIPCION, cls.PRIORIDAD, cls.COMPLETADA]

    @classmethod
    def filter_tareas(cls):
        return {
            cls.NOMBRE: "Nombre",
            cls.DESCRIPCION: "Descripción",
            cls.PRIORIDAD: "Prioridad",
            cls.COMPLETADA: "Completada"
        }


def get_task(id, id_usuario):
    try:
        task = TasksModel.query.filter(TasksModel.id == id, TasksModel.id_usuario == id_usuario).first()
        if task is None:
            raise Exception("Tarea no encontrada")
        return task, None
    except Exception as e:
        return None, f"Error al obtener la tarea: {e}"


def get_tasks_all():
    try:
        tasks = TasksModel.query.all()
        return tasks, None
    except Exception as e:
        return None, f"Error al obtener las tareas: {e}"

def get_tasks_completadas_paginado(page, per_page, id_usuario):
    try:
        tasks_page = TasksModel.query.filter(TasksModel.completada == True, TasksModel.id_usuario == id_usuario).paginate(
            page=page, per_page=per_page, error_out=False
        )
        return tasks_page, None
    except Exception as e:
        return None, f"Error al obtener las tareas completadas: {e}"


def get_tasks_sin_completar_paginado(page, per_page, id_usuario):
    try:
        tasks_page = TasksModel.query.filter(TasksModel.completada == False, TasksModel.id_usuario == id_usuario).paginate(
            page=page, per_page=per_page, error_out=False
        )
        return tasks_page, None
    except Exception as e:
        return None, f"Error al obtener las tareas sin completar: {e}"

def get_tasks_paginado(page, per_page, id_usuario):
    try:
        tasks_page = TasksModel.query.filter(TasksModel.id_usuario == id_usuario).paginate(
            page=page, per_page=per_page, error_out=False
        )
        return tasks_page, None
    except Exception as e:
        return None, f"Error al obtener las tareas: {e}"


def get_filtrar_tareas_paginado(page, per_page, filter, valor):
    try:
        if filter not in FiltrosTareas.get_filter():
            raise Exception("El filtro no existe")

        valor = f"%{valor}%"
        query = TasksModel.query

        match filter:
            case FiltrosTareas.NOMBRE:
                tasks_page = query.filter(TasksModel.nombre.like(valor)).paginate(
                    page=page, per_page=per_page, error_out=False
                )
            case FiltrosTareas.DESCRIPCION:
                tasks_page = query.filter(TasksModel.descripcion.like(valor)).paginate(
                    page=page, per_page=per_page, error_out=False
                )
            case FiltrosTareas.PRIORIDAD:
                tasks_page = query.filter(TasksModel.prioridad.like(valor)).paginate(
                    page=page, per_page=per_page, error_out=False
                )
            case FiltrosTareas.COMPLETADA:
                completada = True if valor.lower() == "true" else False
                tasks_page = query.filter(TasksModel.completada == completada).paginate(
                    page=page, per_page=per_page, error_out=False
                )

        return tasks_page, None
    except Exception as e:
        return None, f"Error al filtrar las tareas: {e}"


def add_task(nombre, descripcion, prioridad, completada=False):
    try:
        task = TasksModel(
            nombre=nombre,
            descripcion=descripcion,
            prioridad=prioridad,
            completada=completada
        )
        db.session.add(task)
        db.session.commit()
        return task.id, None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al guardar la tarea: {e}"


def upd_task(id, data):
    try:
        task = TasksModel.query.filter(TasksModel.id == id).first()
        if task is None:
            raise Exception("Tarea no encontrada")

        task.nombre = data.get('nombre', task.nombre)
        task.descripcion = data.get('descripcion', task.descripcion)
        task.prioridad = data.get('prioridad', task.prioridad)
        task.completada = data.get('completada', task.completada)

        db.session.commit()
        return task.id, None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al actualizar la tarea: {e}"


def del_task(id, id_usuario):
    try:
        task = TasksModel.query.filter(TasksModel.id == id, TasksModel.id_usuario == id_usuario).first()
        if task is None:
            raise Exception("Tarea no encontrada o no pertenece al usuario")

        db.session.delete(task)
        db.session.commit()
        return task.id, None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al eliminar la tarea: {e}"

def upd_task(id, data):
    try:
        task = TasksModel.query.filter(TasksModel.id == id).first()
        if task is None:
            raise Exception("Tarea no encontrada")

        task.nombre = data.get('nombre', task.nombre)
        task.descripcion = data.get('descripcion', task.descripcion)
        task.prioridad = data.get('prioridad', task.prioridad)
        task.completada = data.get('completada', task.completada)

        db.session.commit()
        return task.id, None
    except Exception as e:
        db.session.rollback()
        return None, f"Error al actualizar la tarea: {e}"