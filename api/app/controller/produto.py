from flask import Blueprint, request, jsonify, current_app
from app.model.tables import Produto
from app.schemas.serealizer import ProdutoSchema

bp_produto = Blueprint('produto', __name__)
@bp_produto.route('/cadastrar_produto', methods=['POST'])
def cadastrar_produto():
    ps = ProdutoSchema()
    produto = ps.load(request.json)

    current_app.db.session.add(produto)
    current_app.db.session.commit()

    return ps.jsonify(produto), 201

@bp_produto.route('/mostrar_produtos', methods=['GET'])
def mostrar():
    result = Produto.query.all()
    return ProdutoSchema(many=True).jsonify(result), 200

@bp_produto.route('/mostrar_produto/<identificador>', methods=['GET'])
def mostrar_produto(identificador):
    query = Produto.query.filter(Produto.banca_id == identificador)

    return ProdutoSchema(many=True).jsonify(query), 200

@bp_produto.route('/modificar_produto/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = ProdutoSchema()
    query = Produto.query.filter(Produto.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_produto.route('/deletar_produto/<identificador>', methods=['GET'])
def deletar(identificador):
    Produto.query.filter(Produto.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')