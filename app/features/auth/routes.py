
from flask import Blueprint, render_template, redirect
from app.features.auth.model import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)


@auth.get('/login/')
def login():
    context = {
        "form": LoginForm()
    }
    return render_template('auth/login.jinja', **context)


@auth.post('/login/')
def login_post():
    form: LoginForm = LoginForm()
    if not form.validate_on_submit():
        return render_template('auth/login.jinja', form=form)

    return redirect("/")


@auth.get('/register/')
def register():
    context = {
        "form": RegisterForm()
    }
    return render_template('auth/register.jinja', **context)


@auth.post('/register/')
def register_post():
    form: RegisterForm = RegisterForm()
    if not form.validate_on_submit():

        return render_template('auth/register.jinja', form=form)

    return redirect("/")
