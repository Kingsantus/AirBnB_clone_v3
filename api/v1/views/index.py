#!/usr/bin/python3
"""initializing app views"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object type"""
    classes = ['User', 'Place', 'City', 'Amenity', 'Review', 'State']

    stats = {cls: storage.count(eval(cls)) for cls in classes}
    return jsonify(stats)
