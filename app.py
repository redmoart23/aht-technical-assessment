from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from routes.routes import inventory
from utils.db import db
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(inventory)
