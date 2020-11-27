from flask import Blueprint, request, jsonify, current_app
from app.model.tables import Banca
from app.schemas.serealizer import BancaSchema

bp_banca = Blueprint('banca', __name__)
@bp_banca.route('/cadastrar_banca', methods=['POST'])
def cadastrar():
    bs = BancaSchema()
    banca = bs.load(request.json)
    
    #try:
    #    obj = bs.load(request.json)
    #except ValidationError as error:
    #    print(error.messages)
    
    #if error:
    #    return jsonify(error), 401

    current_app.db.session.add(banca)
    current_app.db.session.commit()
    return bs.jsonify(banca), 201

@bp_banca.route('/mostrar_banca/<identificador>', methods=['GET'])
def mostrar_banca(identificador):
    query = Banca.query.filter(Banca.id == identificador)

    return BancaSchema(many=False).jsonify(query.first()), 200

@bp_banca.route('/mostrar_bancas', methods=['GET'])
def mostrar():
    result = Banca.query.all()
    return BancaSchema(many=True).jsonify(result), 200

@bp_banca.route('/modificar_banca/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = BancaSchema()
    query = Banca.query.filter(Banca.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_banca.route('/deletar_banca/<identificador>', methods=['GET'])
def deletar(identificador):
    Banca.query.filter(Banca.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')
