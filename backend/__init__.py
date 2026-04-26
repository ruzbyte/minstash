from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-duper-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://minstash:!SuperSecret@localhost/minstash"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import backend.db_schema
from backend import routes

with app.app_context():
    db.create_all()
