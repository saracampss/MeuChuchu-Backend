from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from app.model.tables import User, Banca, Produto

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        load_only = ("password",)
        dump_only = ("id")

    name = fields.Str(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    celular = fields.Str(required=False)
    tipo_de_user = fields.Bool(required=False)
    image = fields.Str(required=False)

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

class ProdutoSchema(ma.ModelSchema):
    class Meta:
        model = Produto
        dump_only = ("id")

    name = fields.Str(required=True)
    preco = fields.Float(required=False)
    descricao = fields.Str(required=False)
    banca_id = fields.Int(required=True)