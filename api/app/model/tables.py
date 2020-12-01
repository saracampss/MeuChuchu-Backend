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
    image = db.Column(db.Text, nullable=True)

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
    image = db.Column(db.Text, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user  = db.relationship('User', foreign_keys = user_id)

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Float, nullable=True)
    descricao = db.Column(db.String, nullable=True)
    image = db.Column(db.Text, nullable=True)

    banca_id = db.Column(db.Integer, db.ForeignKey('bancas.id'))
    banca = db.relationship('Banca', foreign_keys = banca_id)
