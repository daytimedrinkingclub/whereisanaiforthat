from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions (e.g., Supabase client) here if needed

    # Register blueprints or routes
    from .routes.routes import main
    app.register_blueprint(main)

    return app