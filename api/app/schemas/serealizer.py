from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from app.model.tables import User

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

"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    celular = db.Column(db.String(11), nullable=False) 
    tipo_de_user = db.Column(db.Boolean, nullable=False)
"""