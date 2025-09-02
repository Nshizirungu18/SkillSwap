from flask import Flask
from app.extensions import db, migrate, jwt
from app.routes.auth import auth_bp
from app.routes.courses import courses_bp
from app.routes.match import match_bp
from app.routes.contact import contact_bp
from app.routes.plans import plans_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(courses_bp, url_prefix='/courses')
    app.register_blueprint(match_bp, url_prefix='/match')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(plans_bp, url_prefix='/plans')

    return app
