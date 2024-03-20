# Internal
import os

# Installed dependencies
from flask import Flask, g, request, jsonify
from flask_cors import CORS

# App imports
from module.services.summary import SummaryService

CORS_ALLOWED_ORIGIN = os.getenv('CORS_ALLOWED_ORIGIN', 'http://localhost:5173').split(',')

def init(app: Flask, summary_service: SummaryService):

    CORS(app, resources={r"/*": {"origins": CORS_ALLOWED_ORIGIN}})

    @app.route('/summary', methods=['POST'])
    def create():
        if not request.json or 'content' not in request.json:
            return jsonify({'error': 'Invalid request'}), 400

        # g object is Flask per-request context
        summary = summary_service.summarize(db=g.db_session, text=request.json['content'])
        return jsonify(summary), 200

    @app.route('/summary', methods=['GET'])
    def read():
        # g object is Flask per-request context
        summaries = summary_service.get_summaries(db=g.db_session)
        return jsonify(summaries), 200

    return app

