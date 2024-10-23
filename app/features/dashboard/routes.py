from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from ..events.models import Evento
from ..notes.model import Nota
from app.features.tasks.controller import get_tasks_paginado
from sqlalchemy import func, case
from datetime import datetime
from ..tasks import TasksModel  # Asegúrate de importar tu modelo de tareas

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index():
    # Obtener la fecha y hora actuales
    now = datetime.now()

    # Consultar los eventos futuros (combinar fecha y hora)
    eventos = Evento.query.filter(
        Evento.usuario_id == current_user.id,
        func.datetime(Evento.fecha, Evento.hora) > now
    ).order_by(
        Evento.fecha.asc(), Evento.hora.asc()
    ).all()

    # Crear datos del evento para pasar al template
    eventos_data = [{'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion, 'fecha': evento.fecha, 'hora': evento.hora} for evento in eventos]

    # Obtener notas
    notas = Nota.query.filter_by(usuario_id=current_user.id).all()
    notas_data = [{'id': nota.id, 'titulo': nota.titulo, 'contenido': nota.contenido} for nota in notas]

    # Obtener solo las tareas no completadas y ordenarlas por prioridad
    page = 1
    per_page = 10

    tasks = TasksModel.query.filter_by(id_usuario=current_user.id, completada=False).order_by(
        case(
            (TasksModel.prioridad == 'alta', 1),
            (TasksModel.prioridad == 'media', 2),
            (TasksModel.prioridad == 'baja', 3)
        )
    ).all()

    # Paginar los resultados
    start = (page - 1) * per_page
    end = start + per_page
    tasks_data = tasks[start:end]

    if not tasks_data and page > 1:
        flash('No hay más tareas disponibles.', 'info')

    return render_template('dashboard/index.jinja', eventos=eventos_data, tasks=tasks_data, notas=notas_data)
