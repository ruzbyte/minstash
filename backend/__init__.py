from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'super-duper-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://minstash:!SuperSecret@localhost/minstash'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False