from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/skillswap_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this later

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register routes (empty for now)
    from app.routes import main
    app.register_blueprint(main)

    return app
