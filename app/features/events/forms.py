from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, TimeField, SubmitField
from wtforms.validators import DataRequired

class EventoForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    hora = TimeField('Hora', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField('Crear Evento')
