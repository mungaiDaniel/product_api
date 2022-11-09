from flask import Flask
from flask_marshmallow import Marshmallow
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:username@localhost/shop'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jefojglueorbum:663eb57afdafbf6fcd05a07607c030812eaf0b3407e26f4017b2af69a9faa81c@ec2-18-215-41-121.compute-1.amazonaws.com:5432/d1a85qu4b3c1bh'
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import model, routes

if __name__ == '__main__':
    app.run()


