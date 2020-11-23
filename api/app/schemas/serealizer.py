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
    password = fields.Str(required=True)
    celular = fields.Str(required=True)
    tipo_de_user = fields.Bool(required=True)
    image = fields.Str(required=True)
