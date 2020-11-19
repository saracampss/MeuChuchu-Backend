from flask import Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from app.model.tables import configure as config_db
from app.schemas.serealizer import configure as config_ma

app = Flask(__name__)

app.config.from_object("app.config.Config")

from app.model.tables import db
migrate = Migrate(app,db)


config_db(app)
config_ma(app)

from app.controller.user import bp_user
app.register_blueprint(bp_user)


#class User(db.Model):
#    __tablename__ = "users"
#
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(128), unique=True, nullable=False)
#    email = db.Column(db.String(128), unique=True, nullable=False)
#    active = db.Column(db.Boolean(), default=True, nullable=False)
#
#    def __init__(self, email, name):
#        self.email = email
#        self.name = name


@app.route("/")
def index():
    return jsonify(Meu="chuchu")