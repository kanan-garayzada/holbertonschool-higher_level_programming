#!/usr/bin/env python3
"""
Task 5 - API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

jwt = JWTManager(app)

# ============================
# In-memory user store
# ============================
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ============================================
# BASIC AUTHENTICATION
# ============================================

@auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials"""
    if username in users:
        stored_hash = users[username]["password"]
        if check_password_hash(stored_hash, password):
            return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ============================================
# JWT ERROR HANDLERS (ALL MUST RETURN 401)
# ============================================

@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.needs_fresh_token_loader
def fresh_token_needed(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

@jwt.revoked_token_loader
def revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


# ============================================
# LOGIN (JWT GENERATION)
# ============================================

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    stored_hash = users[username]["password"]
    if not check_password_hash(stored_hash, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token containing username + role
    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token})


# ============================================
# JWT Protected Route
# ============================================

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ============================================
# ADMIN ONLY ROUTE
# ============================================

@app.route("/admin-only")
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    role = identity.get("role")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ============================================
# RUN SERVER
# ============================================

if __name__ == "__main__":
    app.run()
