from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object('config')
mysql = MySQL()
mysql.init_app(app)
db = SQLAlchemy(app)

from app import views, models