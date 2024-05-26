#!/usr/bin/python3
"""Script of index that view module."""
from api.v1.views import aap_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def api_status():
    """Return status of the API."""
    return jsonify({"status": "OK"})
