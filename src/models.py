from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(120))
    favorites_post = db.Column(db.Integer, ForeignKey('favorites.id'))
    

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

class Favorites (Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_post= Column(Integer, ForeignKey ('planets.id'))
    characters_post = Column(Integer, ForeignKey('characters.id'))
     
    def __repr__(self):
        return 'Favorites < %r>' % self.favorites

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planets_post": self.planets_post,
            "characters_post": self.characters_post,
           
        }
     
     
class Characters (Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    favorites_list = Column(Integer, ForeignKey('favorites.id'))
    comments = Column(String(500)) 

    def __repr__(self):
        return 'Characters < %r>' % self.characters

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favorites_list": self.favorites_list,
            "comments": self.comments,
        }


class Planets (Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    favorites_list = Column(Integer, ForeignKey('favorites.id'))
    user_id = Column(Integer, ForeignKey('user.id')) 
    comments = Column(String(500))

    def __repr__(self):
        return 'Planets < %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favorites_list": self.favorites_list,
            "comments": self.comments,
          
        }   

def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png') 