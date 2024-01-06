#!/usr/bin/python3
"""initializing app views"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object type"""
    stats = {
        'amenities': storage.count("Amenity"),
        'cities': storage.count("City"),
        'places': storage.count("Place"),
        'reviews': storage.count("Review"),
        'states': storage.count("State"),
        'users': storage.count("User"),
    }

    return jsonify(stats)
