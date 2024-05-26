#!/usr/bin/python3

"""Script for a Flask application setup"""


from models import storage
from flask import Flask
from api.v1.view import app_views

app = Flask(__name__)
aap.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the storage connection.
    """
    storage.close

if __name__ == "__main__":
    import os 
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
