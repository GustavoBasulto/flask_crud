from flask import Flask
from flask_app.models.user import User
from flask import flash

app = Flask(__name__)
app.secret_key = "alovio"

