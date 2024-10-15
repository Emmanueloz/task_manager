from flask import Blueprint, render_template, redirect, url_for
from app.features.notes.model import Nota
from app.db import db
from app.features.notes.forms import CrearNotaForm, EditarNotaForm 

notes = Blueprint('notes', __name__)


@notes.get('/notes')
def notes_list():
    notas = Nota.query.all()
    return render_template('notes/lista.jinja', notas=notas)


@notes.get('/notes/create')
def create_note():
    form = CrearNotaForm()
    return render_template('notes/crear.jinja', form=form)


@notes.post('/notes/create')
def guardar_note():
    form = CrearNotaForm()
    if form.validate_on_submit(): 
        titulo = form.titulo.data
        contenido = form.contenido.data

        nueva_nota = Nota(titulo=titulo, contenido=contenido)
        
        nueva_nota.id = 1234 
        
        db.session.add(nueva_nota)
        db.session.commit()


        return redirect(url_for('notes.notes_list'))

    return render_template('notes/crear.jinja', form=form) 

@notes.get('/notes/editar/<int:id>')
def editar_nota(id):
    nota = Nota.query.get_or_404(id)
    form = EditarNotaForm(obj=nota)  
    return render_template('notes/editar.jinja', form=form, nota=nota)

@notes.post('/notes/editar/<int:id>')
def actualizar_nota(id):
    nota = Nota.query.get_or_404(id)
    form = EditarNotaForm()
    
    if form.validate_on_submit(): 
        nota.titulo = form.titulo.data
        nota.contenido = form.contenido.data
        db.session.commit()
        return redirect(url_for('notes.notes_list'))

    return render_template('notes/editar.jinja', form=form, nota=nota) 


@notes.route('/notes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_nota(id):
    nota = Nota.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('notes.notes_list'))
