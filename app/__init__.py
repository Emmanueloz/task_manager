from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.db import db
    db.init_app(app)

    from app.features.dashboard import dashboard
    app.register_blueprint(dashboard)

    from app.features.auth import auth
    app.register_blueprint(auth)

    from app.features.tasks import tasks
    app.register_blueprint(tasks)

    with app.app_context():
        db.create_all()
    return app
