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

    name = fields.Str(required=True)
    email = fields.Email(required=True)
    celular = fields.Str(required=True)
    tipo_de_user = fields.Bool(required=True)
    image = fields.Str(required=True)

class BancaSchema(ma.ModelSchema):
    class Meta:
        model = Banca
        dump_only = ("id")

    name = fields.Str(required=True)
    category = fields.List(fields.Str, required=True)
    user_id = fields.Int(required=True)
    endereco = fields.Str(required=True)

    email = fields.Str(required=True)
    celular = fields.Str(required=True)
    instagram = fields.Str(required=True)
    facebook = fields.Str(required=True)
    website = fields.Str(required=True)
    image = fields.Str(required=True)

class ProdutoSchema(ma.ModelSchema):
    class Meta:
        model = Produto
        dump_only = ("id")

    name = fields.Str(required=True)
    preco = fields.Float(required=False)
    descricao = fields.Str(required=False)
    banca_id = fields.Int(required=True)
    image = fields.Str(required=True)