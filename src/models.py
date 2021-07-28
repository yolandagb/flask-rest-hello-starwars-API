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
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(120))
    # favorites_post = db.Column(db.Integer, ForeignKey('favorites.id'))
    

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
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planets= db.Column(db.Integer, db.ForeignKey ('planets.id'))
    characters= db.Column(db.Integer, db.ForeignKey('characters.id'))
     
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
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    favourites= db.Column (db.Integer, db.ForeignKey('favourites.id'))
    

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
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    favourites= db.Column(db.Integer, db.ForeignKey('favourites.id'))
    

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