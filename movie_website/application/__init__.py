from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "hello"

    with app.app_context():
        from .views import view
        from .user_database import User_db

        app.register_blueprint(view, url_prefix="/")

    return app