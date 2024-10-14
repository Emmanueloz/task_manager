
from flask import Blueprint, render_template, redirect, flash
from app.features.auth.form import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app.features.auth.model import User
from flask_login import login_user, current_user, logout_user
from app.features.auth.login_config import UserLogin
from app.db import db
auth = Blueprint('auth', __name__)


@auth.get('/login/')
def login():
    for user in User.query.all():
        print(f"-{user.email}-")
    context = {
        "form": LoginForm()
    }
    return render_template('auth/login.jinja', **context)


@auth.post('/login/')
def login_post():
    form: LoginForm = LoginForm()

    if not form.validate_on_submit():
        return render_template('auth/login.jinja', form=form)

    email = form.email.data.strip()
    print(f"Email buscado: {email}")
    user = User.query.filter_by(email=email).first()
    print(f"Usuario encontrado: {user}")

    if user is None or not check_password_hash(user.password, form.password.data):
        flash("Usuario o contraseña incorrectos", "danger")
        return render_template('auth/login.jinja', form=form)

    user_login: UserLogin = UserLogin(user)
    login_user(user_login)

    return redirect("/")


@auth.get('/register/')
def register():
    if current_user.is_authenticated:
        return redirect("/")
    context = {
        "form": RegisterForm()
    }
    return render_template('auth/register.jinja', **context)


@auth.post('/register/')
def register_post():
    form: RegisterForm = RegisterForm()
    if not form.validate_on_submit():

        return render_template('auth/register.jinja', form=form)

    try:

        user = User(username=form.username.data, email=form.email.data,
                    password=generate_password_hash(form.password.data))

        db.session.add(user)
        db.session.commit()

        user_login: UserLogin = UserLogin(user)

        login_user(user_login)

        return redirect("/")
    except Exception as e:
        flash("Usuario ya registrado", "warning")
        return render_template('auth/register.jinja', form=form)


@auth.get('/logout/')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")
