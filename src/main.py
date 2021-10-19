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
from models import db, User, Character, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)



# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


##################### Users ##############################################################################
@app.route('/user', methods=['GET'])
def get_users():
    user_query = User.query.all()
    all_user = list(map(lambda x: x.serialize(), user_query))

    return jsonify(all_user), 200

@app.route('/user', methods=['POST'])
def add_new_user():
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'email' not in body:
        raise APIException('You need to specify the email', status_code=400)
    if 'password' not in body:
        raise APIException('You need to specify the password', status_code=400)
    if 'is_active' not in body:
        raise APIException('You need to specify the is_active', status_code=400)           
    user = User(email=body['email'], password=body['password'],is_active=body['is_active'] )
    db.session.add(user)
    db.session.commit()
    return "ok", 200

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user1 = User.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()
    user_query = User.query.all()
    all_user = list(map(lambda x: x.serialize(), user_query))
    return jsonify(all_user), 200



#################################### Characters ########################################################
@app.route('/character', methods=['GET'])
def get_character():
    character_query = Character.query.all()
    all_character = list(map(lambda x: x.serialize(), character_query))

    return jsonify(all_character), 200

# @app.route('/character/<int:id>', methods=['GET'])
# def get_character_index(id):
#     user1 = Character.query.get(id)
#     a_dict = jsons.dump(user1)
#     return a_dict, 200

@app.route('/character', methods=['POST'])
def add_new_character():
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name' not in body:
        raise APIException('You need to specify the name', status_code=400)
    if 'gender' not in body:
        raise APIException('You need to specify the gender', status_code=400)
    if 'hair_color' not in body:
        raise APIException('You need to specify the hair color', status_code=400)
    if 'eye_color' not in body:
        raise APIException('You need to specify the eye color', status_code=400)            
    character1 = Character(name=body['name'], gender=body['gender'], hair_color=body['hair_color'], eye_color=body["eye_color"])
    db.session.add(character1)
    db.session.commit()
    return "ok", 200


@app.route('/character/<int:id>', methods=['DELETE'])
def delete_character(id):
    user1 = Character.query.get(id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user1)
    db.session.commit()
    character_query = Character.query.all()
    all_character = list(map(lambda x: x.serialize(), character_query))
    return jsonify(all_character), 200


################################# Planet ############################################################

@app.route('/planet', methods=['GET'])
def get_planet():
    planet_query = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(), planet_query))

    return jsonify(all_planet), 200

# @app.route('/planet/<int:position>', methods=['GET'])
# def get_planet_index(position):

#     print("This is the position to show: ",position)
    
#     return jsonify(planets[position]), 200

@app.route('/planet', methods=['POST'])
def add_new_planet():
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name' not in body:
        raise APIException('You need to specify the name', status_code=400)
    if 'population' not in body:
        raise APIException('You need to specify the population', status_code=400)
    if 'terrain' not in body:
        raise APIException('You need to specify the terrain', status_code=400)        
    planet = Planet(name=body['name'], population=body['population'], terrain=body['terrain'])
    db.session.add(planet)
    db.session.commit()
    return "ok", 200



@app.route('/planet/<int:id>', methods=['DELETE'])
def delete_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(planet)
    db.session.commit()
    planet_query = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(), planet_query))

    return jsonify(all_planet), 200


####################################### Vehicle #################################################

@app.route('/vehicle', methods=['GET'])
def get_vehicle():
    vehicle_query = Vehicle.query.all()
    all_vehicle = list(map(lambda x: x.serialize(), vehicle_query))

    return jsonify(all_vehicle), 200

# @app.route('/vehicle/<int:position>', methods=['GET'])
# def get_vehicle_index(position):

#     print("This is the position to show: ",position)
    
#     return jsonify(vehicles[position]), 200

@app.route('/vehicle', methods=['POST'])
def add_new_vehicle():
    body = request.get_json()
    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'name' not in body:
        raise APIException('You need to specify the name', status_code=400)
    if 'vehicle_class' not in body:
        raise APIException('You need to specify the vehicle class', status_code=400)
    if 'manufacturer' not in body:
        raise APIException('You need to specify the manufacturer', status_code=400)        
    vehicle = Vehicle(name=body['name'], vehicle_class=body['vehicle_class'], manufacturer=body['manufacturer'])
    db.session.add(vehicle)
    db.session.commit()
    vehicles.append(body)
    return "ok", 200


@app.route('/vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(vehicle)
    db.session.commit()
    vehicle_query = vehicle.query.all()
    all_vehicle = list(map(lambda x: x.serialize(), vehicle_query))

    return jsonify(all_vehicle), 200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
