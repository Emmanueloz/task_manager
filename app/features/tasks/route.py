from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask_login import login_required, current_user  # Asegúrate de importar login_required y current_user
from app.features.tasks.controller import *

tasks = Blueprint('TaskRoute', __name__)

@tasks.get('/tasks')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    filtro = request.args.get('filtro', 'todos')
    per_page = 10
    tasks_page = None
    error = None

    if filtro == 'completados':
        tasks_page, error = get_tasks_completadas_paginado(page, per_page, current_user.id)
    elif filtro == 'sin_completar':
        tasks_page, error = get_tasks_sin_completar_paginado(page, per_page, current_user.id)
    else:
        tasks_page, error = get_tasks_paginado(page, per_page, current_user.id)

    if error is not None:
        flash(f"Error al obtener las tareas: {error}", "error")

    all_tasks = tasks_page.items if tasks_page else []

    context = {
        "tasks_page": tasks_page,
        "all_tasks": all_tasks,
        "filtro": filtro,
    }
    return render_template('tasks/index.jinja2', **context)

@tasks.get('/tasks/create')
@login_required
def create():
    return render_template('tasks/formulario.jinja2')

@tasks.post('/tasks/create')
@login_required
def create_task():
    nombre = request.form.get('taskName')
    descripcion = request.form.get('description')
    prioridad = request.form.get('priority')

    nueva_tarea = TasksModel(
        id=None,
        nombre=nombre,
        descripcion=descripcion,
        prioridad=prioridad,
        completada=False,
        id_usuario=current_user.id
    )

    try:
        db.session.add(nueva_tarea)
        db.session.commit()
        flash('Tarea creada con éxito.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al crear la tarea: {e}', 'error')

    return redirect(url_for('TaskRoute.index'))

@tasks.get('/tasks/edit/<int:task_id>')
@login_required
def edit(task_id):
    task, error = get_task(task_id, current_user.id)  
    if error:
        flash(error, 'error')
        return redirect(url_for('TaskRoute.index'))
    return render_template('tasks/formulario.jinja2', task=task)

@tasks.post('/tasks/edit/<int:task_id>')
@login_required
def edit_task(task_id):
    task, error = get_task(task_id, current_user.id)  
    if error:
        flash(error, 'error')
        return redirect(url_for('TaskRoute.index'))

    nombre = request.form.get('taskName')
    descripcion = request.form.get('description')
    prioridad = request.form.get('priority')

    _, error = upd_task(task_id, {
        'nombre': nombre,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'completada': task.completada
    })

    if error:
        flash(f'Error al actualizar la tarea: {error}', 'error')
    else:
        flash('Tarea actualizada con éxito.', 'success')

    return redirect(url_for('TaskRoute.index'))

@tasks.post('/tasks/toggle/<int:task_id>')
@login_required
def toggle_task(task_id):
    task, error = get_task(task_id, current_user.id)  
    if error:
        flash(error, 'error')
        return redirect(url_for('TaskRoute.index'))

    completada = request.form.get('completada') == '1'
    _, error = upd_task(task_id, {
        'nombre': task.nombre,
        'descripcion': task.descripcion,
        'prioridad': task.prioridad,
        'completada': completada
    })

    if error:
        flash(f'Error al actualizar la tarea: {error}', 'error')
    else:
        flash('Estado de la tarea actualizado con éxito.', 'success')

    return redirect(url_for('TaskRoute.index'))

@tasks.get('/tasks/<int:id>/eliminar')
@login_required
def get_eliminar(id):
    task, error = del_task(id, current_user.id)  
    if error is not None:
        flash(f"Error {error}", "error")
        return redirect(url_for('TaskRoute.index'))

    flash("Tarea eliminada correctamente", "message")
    return redirect(url_for('TaskRoute.index'))
