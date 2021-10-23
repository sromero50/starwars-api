from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_characters = db.relationship('FavoriteCharacter', passive_deletes=True, back_populates="user")
    favorite_planets = db.relationship('FavoritePlanet', passive_deletes=True, back_populates="user")
    favorite_vehicles = db.relationship('FavoriteVehicle', passive_deletes=True, back_populates="user")
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorite_characters": list(map(lambda x: x.serialize(), self.favorite_characters)),
            "favorite_planets": list(map(lambda x: x.serialize(), self.favorite_planets)),
            "favorite_vehicles": list(map(lambda x: x.serialize(), self.favorite_vehicles))
        }



class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(150), nullable=False)
    hair_color = db.Column(db.String(150), nullable=False)
    eye_color = db.Column(db.String(150),  nullable=False)
    

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    vehicle_class = db.Column(db.String(150), nullable=False)
    manufacturer = db.Column(db.String(150), nullable=False)

    
    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer
        }

class FavoriteCharacter(db.Model):
    __tablename__ = 'favoriteCharacter'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id', ondelete='CASCADE'))
    user = db.relationship(User, back_populates="favorite_characters")
    character = db.relationship(Character)


    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id
        }

class FavoritePlanet(db.Model):
    __tablename__ = 'favoritePlanet'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id', ondelete='CASCADE'))
    user = db.relationship(User, back_populates="favorite_planets")
    planet = db.relationship(Planet)


    def __repr__(self):
        return '<FavoritePlanet %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }

class FavoriteVehicle(db.Model):
    __tablename__ = 'FavoriteVehicle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id', ondelete='CASCADE'))
    user = db.relationship(User, back_populates="favorite_vehicles")
    vehicle = db.relationship(Vehicle)


    def __repr__(self):
        return '<FavoriteVehicle %r>' % self.id


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id
        }


# class Favorite(db.Model):
#     __tablename__ = 'favorite'
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     fav_character_id = db.Column(db.Integer, db.ForeignKey('favoriteCharacter.id'))
#     fav_planet_id = db.Column(db.Integer, db.ForeignKey('favoritePlanet.id'))
#     fav_vehicle_id = db.Column(db.Integer, db.ForeignKey('FavoriteVehicle.id'))
#     user = db.relationship(User)
#     favorite_characters = db.relationship('FavoriteCharacter')
#     favorite_planets = db.relationship('FavoritePlanet')
#     favorite_vehicles = db.relationship('FavoriteVehicle')
    

#     def __repr__(self):
#         return '<Favorite %r>' % self.user_id


#     def serialize(self):
#         return {
#             "user_id": self.user_id,
#             "favorite_characters": list(map(lambda x: x.serialize(), self.favorite_characters)),
#             "favorite_planets": list(map(lambda x: x.serialize(), self.favorite_planets)),
#             "favorite_vehicles": list(map(lambda x: x.serialize(), self.favorite_vehicles))

#         }
