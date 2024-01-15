#!/usr/bin/python3
""" Starts a Flask Web Application """

# Import necessary modules and classes from the project
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid

# Create a Flask web application
app = Flask(__name__)
# Uncomment the lines below to configure Jinja template options
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

# Define a function to close the SQLAlchemy session when the application context is torn down
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

# Define a route for the '/0-hbnb/' endpoint
@app.route('/0-hbnb/', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """

    # Retrieve all states from the storage and sort them alphabetically
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    strict = []

    # Create a list of states and their corresponding cities, sorted alphabetically
    for state in states:
        strict.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Retrieve all amenities from the storage and sort them alphabetically
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Retrieve all places from the storage and sort them alphabetically
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Generate a random UUID as a cache identifier
    cached_id = uuid.uuid4()

    # Render the '0-hbnb.html' template with the data obtained above
    return render_template('0-hbnb.html',
                           states=strict,
                           amenities=amenities,
                           places=places,
                           cache_id=cached_id)

# Run the application if the script is executed directly
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
