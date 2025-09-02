from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__)

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and check_password_hash(user.password_hash, data["password"]):
        token = create_access_token(identity=user.id)
        return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
