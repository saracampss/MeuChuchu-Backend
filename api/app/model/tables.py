from flask_sqlalchemy import SQLAlchemy
#from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(11), nullable=False) 
    tipo_de_user = db.Column(db.Boolean, nullable=False)

