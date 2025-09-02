from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.Text)
    role = db.Column(db.String(20))  # 'learner' or 'instructor'
    plan = db.Column(db.String(20))  # 'free', 'premium', 'ai'
    created_at = db.Column(db.DateTime, server_default=db.func.now())
