from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.features.notes.model import Nota
from app.db import db


notes = Blueprint('notes', __name__)



@notes.get('/notes')
def notes_list():

    notas = Nota.query.all()
    return render_template('notes/lista.jinja', notas=notas)


@notes.get('/notes/create')
def create_note():
    return render_template('notes/crear.jinja')


@notes.post('/notes/create')
def guardar_note():
    titulo =request.form.get('titulo')
    contenido =request.form.get('contenido')

    id_notes= 11

    nueva_nota = Nota(id=id_notes, titulo=titulo, contenido=contenido)

    db.session.add(nueva_nota)
    db.session.commit()


    return redirect(url_for('notes.notes_list'))


@notes.get('/notes/editar/<int:id>')
def editar_nota(id):
    nota = Nota.query.get_or_404(id)
    return render_template('notes/editar.jinja', nota=nota)

@notes.post('/notes/editar/<int:id>')
def actualizar_nota(id):
    nota = Nota.query.get_or_404(id)
    nota.titulo = request.form.get('titulo')
    nota.contenido = request.form.get('contenido')
    
    db.session.commit()
    flash('Nota actualizada con éxito.')
    return redirect(url_for('notes.notes_list'))


@notes.route('/notes/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar_nota(id):
    nota = Nota.query.get_or_404(id)
    db.session.delete(nota)
    db.session.commit()
    flash('Nota eliminada con éxito.')
    return redirect(url_for('notes.notes_list'))

