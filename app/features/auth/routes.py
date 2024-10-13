
from flask import Blueprint, render_template, redirect
from app.features.auth.model import LoginForm

auth = Blueprint('auth', __name__)


@auth.get('/login/')
def login():
    form: LoginForm = LoginForm()
    context = {
        "form": form
    }
    return render_template('auth/login.jinja', **context)


@auth.post('/login/')
def login_post():
    return redirect("/")


@auth.get('/register/')
def register():
    return render_template('auth/register.jinja')


@auth.post('/register/')
def register_post():
    return redirect("/")
