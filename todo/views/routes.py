from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

# Health endpoint

@api.route('/health')
def health():
    return jsonify({"status": "ok"})