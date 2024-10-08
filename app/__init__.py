from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.features.dashboard import dashboard
    app.register_blueprint(dashboard)

    return app
