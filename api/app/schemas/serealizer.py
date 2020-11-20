from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from app.model.tables import User, Banca 

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id")

    name = fields.Str(required=True)
    email = fields.Email(required=True)
    celular = fields.Str(required=True)
    tipo_de_user = fields.Bool(required=True)

class BancaSchema(ma.ModelSchema):
    class Meta:
        model = Banca
        dump_only = ("id")

    name = fields.Str(required=True)
    category = fields.List(fields.Str, required=True)
    user_id = fields.Int(required=True)
    
    email = fields.Email(required=False)
    celular = fields.Str(required=False)
    instagram = fields.Url(required=False)
    facebook = fields.Url(required=False)
    website = fields.Url(required=False)
    

"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.ARRAY(db.String), nullable=False)
    regadm = db.Column(db.String(50), nullable=False)
    
    #Contatos
    email = db.Column(db.String(320), nullable=True, unique=True)
    celular = db.Column(db.String(11), nullable=True) 
    instagram = db.Column(db.String, nullable=True) 
    facebook = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user  = db.relationship('User', foreign_keys = user_id)

    List
    Url
    Email
"""