# Internal
import os

# Installed dependencies
from flask import Flask, request, jsonify
from flask_cors import CORS

# App imports
from module.services.summary import SummaryService

CORS_ALLOWED_ORIGIN = os.getenv('CORS_ALLOWED_ORIGIN', 'http://localhost:5173').split(',')

def init(summary_service: SummaryService):
    app = Flask(__name__)

    CORS(app, resources={r"/*": {"origins": CORS_ALLOWED_ORIGIN}})

    @app.route('/summary', methods=['POST'])
    def create():
        if not request.json or 'content' not in request.json:
            return jsonify({'error': 'Invalid request'}), 400

        summary = summary_service.summarize(request.json['content'])
        return jsonify(summary), 200

    @app.route('/summary', methods=['GET'])
    def read():
        summaries = summary_service.get_summaries()
        return jsonify(summaries), 200

    return app

