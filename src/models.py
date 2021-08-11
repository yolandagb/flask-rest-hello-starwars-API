from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    # id = db.Column(db.Integer, primary_key=True)
    # nickname = db.Column(db.String(250))
    # email = db.Column(db.String(250), nullable=False)
    # password = db.Column(db.String(120))
    # # favorites_post = db.Column(db.Integer, ForeignKey('favorites.id'))
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), unique=True, nullable=False)
    first_name =Column(String(100), nullable=False)
    last_name =Column(String(100), nullable=False)
    created_at =Column(String(20))
    updated_at =Column(String(20))
    email =Column(String(80),unique=True, nullable=False) 
    
    # RELATIONSHIP
    favorites = relationship('Favorite', backref="user", lazy=True)
    characters = relationship('Character', backref="user", lazy=True)
    planets = relationship('Planet', backref="user", lazy=True)
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "favorites_post": self.favorites_post,
            # do not serialize the password, its a security breach
        }

class Favourites(db.Model):
    __tablename__ = 'favorites'
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # planets= db.Column(db.Integer, db.ForeignKey ('planets.id'))
    # characters= db.Column(db.Integer, db.ForeignKey('characters.id'))
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    fav_planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    fav_character_id = Column(Integer, ForeignKey('character.character_id'))
     
    def __repr__(self):
        return 'Favorites < %r>' % self.favorites

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets": self.planets,
            "characters": self.characters,
           
        }
     
     
class Characters(db.Model):
    __tablename__ = 'characters'
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    # favourites= db.Column (db.Integer, db.ForeignKey('favourites.id'))
    id = Column(Integer, primary_key=True)
    name =  Column(String(200))
    birth_year = Column(Integer)
    gender = Column(String(200))
    height = Column(Integer)
    skin_color = Column(String(200))
    eye_color = Column(String(200))
    

    def __repr__(self):
        return 'Characters < %r>' % self.characters

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favourites": self.favourites,
            
        }


class Planets(db.Model):
    __tablename__ = 'planets'
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    # favourites= db.Column(db.Integer, db.ForeignKey('favourites.id'))
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    climate = Column(String(200))
    population = Column(Integer)
    orbital_period = Column(Integer)
    diameter= Column(Integer)

    

    def __repr__(self):
        return 'Planets < %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favourites": self.favourites,
            
          
        }   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(db.Model, 'diagram.png')