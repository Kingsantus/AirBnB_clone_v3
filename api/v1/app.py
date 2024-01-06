#!/usr/bin/python3
"""Flask initiation file"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exec):
    """teardown method
    """
    storage.close()

if __name__ == "__main__":
    app.run(host=getenv(HBNB_API_HOST),
            port=getenv(HBNB_API_PORT),
            threaded=True)
