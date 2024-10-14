from flask import render_template, redirect, request, url_for, flash
from . import events_bp  
from .models import Evento
from .forms import EventoForm
from app.db import db 

@events_bp.route('/events', methods=['GET'])
def list_events():
    eventos = Evento.query.all()
    return render_template('events/list_events.jinja', eventos=eventos)

@events_bp.route('/event/create', methods=['GET', 'POST'])
def create_event():
    form = EventoForm()
    if form.validate_on_submit():
        nuevo_evento = Evento(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            fecha=form.fecha.data,
            hora=form.hora.data
        )
        db.session.add(nuevo_evento)
        db.session.commit()
        flash('Evento creado exitosamente.')
        return redirect(url_for('events.list_events'))  
    else:
        print("Errores en el formulario:", form.errors)  
    return render_template('events/create_event.jinja', form=form)

@events_bp.route('/event/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    evento = Evento.query.filter_by(id=id).first()  
    if not evento:
        flash('Evento no encontrado.')  
        return redirect(url_for('events.list_events'))  

    form = EventoForm(obj=evento)  # Pasa el evento al formulario

    if form.validate_on_submit():
        evento.titulo = form.titulo.data
        evento.descripcion = form.descripcion.data
        evento.fecha = form.fecha.data
        evento.hora = form.hora.data

        db.session.commit()  
        flash('Evento editado exitosamente.')  
        return redirect(url_for('events.list_events'))  

    return render_template('events/edit_event.jinja', form=form, evento=evento)  

@events_bp.route('/event/delete/<int:id>', methods=['GET', 'POST'])
def delete_event(id):
    evento = Evento.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(evento)
        db.session.commit()
        flash('Evento eliminado exitosamente.')
        return redirect(url_for('events.list_events'))
    
    return render_template('events/delete_event.jinja2', evento=evento)