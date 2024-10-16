from flask import Blueprint, render_template, request, redirect, url_for
from app.features.notes.model import Nota
from app.db import db
from app.features.notes.forms import NotaForm 
from flask_login import login_required, current_user

notes = Blueprint('notes', __name__)

@notes.get('/notes')
@login_required
def notes_list():
    notas = Nota.query.filter_by(usuario_id=current_user.id).all()
    return render_template('notes/lista.jinja', notas=notas)


@notes.get('/notes/create')
@login_required
def create_note():
    form = NotaForm()
    return render_template('notes/crear.jinja', form=form)


@notes.post('/notes/create')
@login_required
def guardar_note():
    form = NotaForm() 
    if form.validate_on_submit():
        nueva_nota = Nota(titulo=form.titulo.data, contenido=form.contenido.data, usuario_id=current_user.id)
        db.session.add(nueva_nota)
        db.session.commit()
        return redirect(url_for('notes.notes_list'))
    return render_template('notes/crear.jinja', form=form) 


@notes.get('/notes/editar/<int:id>')
@login_required
def editar_nota(id):
    nota = Nota.query.filter_by(id=id, usuario_id=current_user.id).first()
    form = NotaForm(obj=nota) 
    return render_template('notes/editar.jinja', form=form, nota=nota)

@notes.post('/notes/editar/<int:id>')
@login_required
def actualizar_nota(id):
    nota = Nota.query.get_or_404(id)
    form = NotaForm()  
    if form.validate_on_submit():
        nota.titulo = form.titulo.data
        nota.contenido = form.contenido.data
        db.session.commit()
        return redirect(url_for('notes.notes_list'))
    return render_template('notes/editar.jinja', form=form, nota=nota)

@notes.route('/notes/eliminar/<int:id>', methods=['GET', 'POST'])
@login_required
def eliminar_nota(id):
    nota = Nota.query.filter_by(id=id, usuario_id=current_user.id).first()
    db.session.delete(nota)
    db.session.commit()
    return redirect(url_for('notes.notes_list'))
