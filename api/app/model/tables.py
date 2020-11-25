from flask_sqlalchemy import SQLAlchemy
#from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db



class Banca(db.Model):
    __tablename__ = "bancas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.ARRAY(db.String), nullable=False)
    endereco = db.Column(db.String, nullable=False)
    regadm = db.Column(db.String(50), nullable=False)
    
    #Contatos
    email = db.Column(db.String(320), nullable=True, unique=True)
    celular = db.Column(db.String(11), nullable=True) 
    instagram = db.Column(db.String, nullable=True) 
    facebook = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user  = db.relationship('User', foreign_keys = user_id)