from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


# class Home (Base):
#      __tablename__ = 'home'
#      id = Column(Integer, primary_key=True)
#      password = Column(Integer, ForeignKey('Login.Password'))
#      user_name =  Column(Integer, ForeignKey('User.user_name'))
#      url = Column(String(250), nullable=False)
#      user_id = Column(Integer, ForeignKey('user.id'))
#      post = Column(Integer, ForeignKey('post.id'))
#      planets_post = Column(Integer, ForeignKey('planets.post'))
#      characters_post = Column(Integer, ForeignKey('characters.post'))
     

# class User(Base):
#      __tablename__ = 'User'
#      id = Column(Integer, primary_key=True)
#      username = Column(String(250))
#      password = Column(Integer, ForeignKey('Login.password'))
#      email = Column(String(250), nullable=False)
#      post = Column(Integer, ForeignKey('post.id'))

# class Like (Base):
#      __tablename__ = 'like'
#      # Here we define columns for the table address.
#      # Notice that each column is also a normal Python instance attribute.
#      id = Column(Integer, primary_key=True)
#      likes = Column(String(250))
#      user_id = Column(Integer, ForeignKey('post.id'))
#      like = Column(Integer, ForeignKey('like.id'))
#      planets_post = Column(Integer, ForeignKey ('planets.post'))
#      characters_post = Column(Integer, ForeignKey('characters.post'))
     
# class Characters (Base):
#      __tablename__ = 'characters'
#      # Here we define columns for the table address.
#      # Notice that each column is also a normal Python instance attribute.
#      id = Column(Integer, primary_key=True)
#      likes = Column(String(250))
#      user_id = Column(Integer, ForeignKey('user.id'))
#      like = Column(Integer, ForeignKey('like.id'))
#      user = relationship ('User')    