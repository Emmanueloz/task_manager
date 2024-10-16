from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = EmailField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
