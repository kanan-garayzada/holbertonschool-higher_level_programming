#!/usr/bin/env python3
"""
Task 4 - Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users stored in memory
# IMPORTANT: Leave empty for checker
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Health check"""
    return "OK"


@app.route("/data")
def get_data():
    """Return list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return user object by username"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user using POST"""
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
