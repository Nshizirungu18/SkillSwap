from flask import Flask
from .config import Config
from .extensions import db, migrate, jwt
from .routes import auth_routes, user_routes, course_routes, match_routes, payment_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_routes.bp, url_prefix="/api/auth")
    app.register_blueprint(user_routes.bp, url_prefix="/api/users")
    app.register_blueprint(course_routes.bp, url_prefix="/api/courses")
    app.register_blueprint(match_routes.bp, url_prefix="/api/match")
    app.register_blueprint(payment_routes.bp, url_prefix="/api/payments")

    return app
