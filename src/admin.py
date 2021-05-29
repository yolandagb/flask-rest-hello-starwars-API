import os
from flask_admin import Admin
from models import db, User,Favorites, Characters, Planets
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Favorites, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Planets, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))

# from flask import Flask, jsonify, request
# import json
# app = Flask(__name__)

# todos = [
#     { "label": "My first task", "done": False },
#     { "label": "My second task", "done": False }
#     ]
# @app.route('/todoss', methods=['GET'])
# def hello_world():
#     return jsonify(todos)

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = json.loads(request.data)
#     todos.append(request_body)
#     return jsonify(todos)
     