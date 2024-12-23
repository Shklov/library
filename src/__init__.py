from flask import Flask
from src.controllers.book_controller import book_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(book_bp)
    return app
