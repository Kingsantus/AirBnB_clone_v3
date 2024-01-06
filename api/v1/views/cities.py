#!/usr/bin/python3
"""creating CRUD route for cites"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'], strict_slashes=False)
def city_route(state_id):
    cities = storage.all(City)
    states = storage.all(State)

    if request.method == "GET":
        """Retrieves the list of all City objects of a State"""
        state_key = "State." + state_id
        try:
            state = states[state_key]
            cities_list = [city.to_dict() for city in state.cities]
            return jsonify(cities_list)
        except KeyError:
            abort(404)

    elif request.method == "POST":
        """Creates a City"""
        if request.is_json:
            body_request = request.get_json()
        else:
            abort(400, "Not a JSON")
        if 'name' in body_request:
            state_key = "State." + state_id
            if state_key not in states:
                abort(404)
            body_request.update({"state_id": state_id})
            new_city = City(**body_request)
            storage.new(new_city)
            storage.save()
            return jsonify(new_city.to_dict()), 201
        else:
            abort(400, "Missing name")

@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def cities_id_mothods(city_id):
    """Retrieves a City object with GET"""
    cities = storage.all(City)

    if request.method == "GET":
        """Retrieves a City object"""
        if not city_id:
            return jsonify([obj.to_dict() for obj in cities.values()])
        key = "City." + city_id
        try:
            return jsonify(cities[key].to_dict())
        except KeyError:
            abort(404)
    
    elif request.method == "DELETE":
        """Deletes a City object"""
        try:
            key = "City." + city_id
            storage.delete(cities[key])
            storage.save()
            return jsonify({}), 200
        except:
            abort(404)

    elif request.method == "PUT":
        """Updates a City object"""
        city_key = "City." + city_id
        try:
            city = cities[city_key]
        except KeyError:
            abort(404)
        if request.is_json:
            new = request.get_json()
        else:
            abort(400, "Not a JSON")
        for key, value in new.items():
            if key != "id" and key != "state_id" and key != "created_at" and\
               key != "updated_at":
                setattr(city, key, value)
            storage.save()
            return city.to_dict(), 200
