from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from ..events.models import Evento
from ..notes.model import Nota # Importamos el modelo Nota
from app.features.tasks.controller import get_tasks_paginado

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index():
    eventos = Evento.query.filter_by(usuario_id=current_user.id).all()
    eventos_data = [{'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion} for evento in eventos]

    notas = Nota.query.filter_by(usuario_id=current_user.id).all()
    notas_data = [{'id': nota.id, 'titulo': nota.titulo, 'contenido': nota.contenido} for nota in notas]

    page = 1
    per_page = 10

    
    tasks_page, error = get_tasks_paginado(page, per_page, current_user.id)

    if error:
        flash(f'Error al obtener las tareas: {error}', 'error')
        tasks_data = []
    else:
        tasks_data = tasks_page.items if tasks_page else []

    return render_template('dashboard/index.jinja', eventos=eventos_data, tasks=tasks_data, notas=notas_data)
