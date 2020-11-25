import os
from flask import Flask, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from app.model.tables import configure as config_db
from app.schemas.serealizer import configure as config_ma

app = Flask(__name__)

app.config.from_object("app.config.Config")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SECURITY_PASSWORD"] = app.config["SECRET_KEY"]


from app.model.tables import db
migrate = Migrate(app,db)


config_db(app)
config_ma(app)
login_manager = LoginManager()
login_manager.init_app(app)

from app.controller.user import bp_user
app.register_blueprint(bp_user)

from app.controller.banca import bp_banca
app.register_blueprint(bp_banca)


@app.route("/")
def index():
    return jsonify(Meu="chuchu")