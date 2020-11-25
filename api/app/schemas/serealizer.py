from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from app.model.tables import User, Banca 

ma = Marshmallow()

def configure(app):
    ma.init_app(app)




class BancaSchema(ma.ModelSchema):
    class Meta:
        model = Banca
        dump_only = ("id")

    name = fields.Str(required=True)
    category = fields.List(fields.Str, required=True)
    user_id = fields.Int(required=True)
    endereco = fields.Str(required=True)
    
    email = fields.Str(required=False)
    celular = fields.Str(required=False)
    instagram = fields.Str(required=False)
    facebook = fields.Str(required=False)
    website = fields.Str(required=False)