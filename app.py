from flask import Flask, render_template
from routes.routes import inventory

app = Flask(__name__)

app.register_blueprint(inventory)
