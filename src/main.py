"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import flask
import json
from flask import Flask, request, jsonify, url_for
from flask import request
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

characters = [{"id":"0", "name":"Luke", "gender":"male", "hair_color":"blonde", "eye_color":"green"}]

planets = [{"id":"0", "name":"Tatooine", "population":"1000000", "terrain":"desert"}]

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return response_body, 200

@app.route('/character', methods=['GET'])
def get_character():

    response_body = flask.jsonify(characters)

    return response_body, 200

@app.route('/character/<int:position>', methods=['GET'])
def get_character_index(position):

    print("This is the position to show: ",position)
    
    return jsonify(characters[position])

@app.route('/character', methods=['POST'])
def add_new_character():
    request_body = request.data
    request_decodificado = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    if isinstance(request_decodificado, list):
        for i in request_decodificado:
            characters.append(i)
    elif isinstance(request_decodificado, dict):
        characters.append(request_decodificado)
    else: 
        return print("error 400")
    return jsonify(characters)


@app.route('/character/<int:position>', methods=['DELETE'])
def delete_character(position):
    print("This is the position to delete: ",position)
    
    characters.pop(position)
    
    return jsonify(characters)


@app.route('/planet', methods=['GET'])
def get_planet():

    response_body = flask.jsonify(planets)

    return response_body, 200

@app.route('/planet/<int:position>', methods=['GET'])
def get_planet_index(position):

    print("This is the position to show: ",position)
    
    return jsonify(planets[position])

@app.route('/planet', methods=['POST'])
def add_new_planet():
    request_body = request.data
    request_decodificado = json.loads(request_body)
    print("Incoming request with the following body", request_body)
    if isinstance(request_decodificado, list):
        for i in request_decodificado:
            planets.append(i)
    elif isinstance(request_decodificado, dict):
        planets.append(request_decodificado)
    else: 
        return print("error 400")
    return jsonify(planets)


@app.route('/planet/<int:position>', methods=['DELETE'])
def delete_planet(position):
    print("This is the position to delete: ",position)
    
    planets.pop(position)
    
    return jsonify(planets)



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
