from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = "root"
# app.config['MYSQL_DATABASE_PASSWORD'] = "bhava"
# app.config['MYSQL_DATABASE_DB'] = "EmpData"
# app.config['MYSQL_DATABASE_HOST'] = "localhost"
# mysql.init_app(app)

from app import views, models