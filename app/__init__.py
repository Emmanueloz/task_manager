from flask import Flask
from flask_migrate import Migrate
from .config import Config
from app.db import db
from app.features.dashboard import dashboard
from app.features.auth import auth
from app.features.events import events_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.features.auth import login_manager
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(dashboard)
    app.register_blueprint(auth)
    app.register_blueprint(events_bp)

    from app.features.tasks import tasks
    app.register_blueprint(tasks)

    with app.app_context():
        db.create_all()
    return app
