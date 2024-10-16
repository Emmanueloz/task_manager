from flask import Blueprint, request, render_template, flash, redirect, url_for  # Asegúrate de incluir 'request', 'redirect', y 'url_for'
from app.features.tasks.controller import *

tasks = Blueprint('TaskRoute', __name__)

@tasks.get('/tasks')
def index():
    page = request.args.get('page', 1, type=int)
    filtro = request.args.get('filtro', 'todos')
    per_page = 10
    tasks_page = None
    error = None

    if filtro == 'completados':
        tasks_page, error = get_tasks_completadas_paginado(page, per_page)
    elif filtro == 'sin_completar':
        tasks_page, error = get_tasks_sin_completar_paginado(page, per_page)
    else:  # Caso por defecto 'todos'
        tasks_page, error = get_tasks_paginado(page, per_page)

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
def create():
    return render_template('tasks/formulario.jinja2')

@tasks.post('/tasks/create')
def create_task():
    nombre = request.form.get('taskName')
    descripcion = request.form.get('description')
    prioridad = request.form.get('priority')

    nueva_tarea = TasksModel(
        id= None,
        nombre=nombre,
        descripcion=descripcion,
        prioridad=prioridad,
        completada=False,
        id_usuario=1 
    )

    try:
        db.session.add(nueva_tarea)
        db.session.commit()           
        flash('Tarea creada con éxito.', 'success')
    except Exception as e:
        db.session.rollback()   
        flash('Error al crear la tarea: {}'.format(e), 'error')  

    return redirect(url_for('TaskRoute.index'))




@tasks.get('/tasks/edit/<int:task_id>')
def edit(task_id):
    task, error = get_task(task_id)
    if error:
        flash(error, 'error')
        return redirect(url_for('TaskRoute.index'))
    return render_template('tasks/formulario.jinja2', task=task)

@tasks.post('/tasks/edit/<int:task_id>')
def edit_task(task_id):
    task, error = get_task(task_id)
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
def toggle_task(task_id):
    task, error = get_task(task_id)
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
def get_eliminar(id):
    task, error  = del_task(id)
    if error is not None:
        flash(f"Error {error}", "error")
        return redirect(url_for('TaskRoute.index'))

    flash(f"Tarea eliminada correctamente", "message")
    return redirect(url_for('TaskRoute.index'))
