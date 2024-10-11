from flask import Blueprint, render_template

tasks = Blueprint('TaskRoute', __name__)
@tasks.get('/tasks')
def index():
    return render_template('tasks/index.jinja2')

@tasks.get('/tasks/create')
def create():
    return render_template('tasks/formulario.jinja2')

@tasks.get('/tasks/edit')
def edit():
    return render_template('tasks/list.jinja2')

