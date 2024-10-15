from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NotaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    contenido = TextAreaField('Contenido', validators=[DataRequired()])
    submit = SubmitField('Guardar')
