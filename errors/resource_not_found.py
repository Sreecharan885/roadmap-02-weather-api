from flask import jsonify
from app import app

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({"error": "Invalid API call"}), 400