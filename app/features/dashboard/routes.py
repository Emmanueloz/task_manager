from flask import Blueprint, render_template
from ..events.models import Evento
from app.db import db
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index():
    # Obtener los eventos del usuario actual
    eventos = Evento.query.filter_by(usuario_id=current_user.id).all()
    # Extraer títulos, descripciones y el id de los eventos
    eventos_data = [{'id': evento.id, 'titulo': evento.titulo, 'descripcion': evento.descripcion} for evento in eventos]
    return render_template('dashboard/index.jinja', eventos=eventos_data)
