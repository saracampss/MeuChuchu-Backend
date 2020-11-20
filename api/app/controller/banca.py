from flask import Blueprint, request, jsonify, current_app
from app.model.tables import Banca
from app.schemas.serealizer import BancaSchema

bp_banca = Blueprint('banca', __name__)
@bp_banca.route('/mostrar', methods=['GET'])
def mostrar():
    result = Banca.query.all()
    return BancaSchema(many=True).jsonify(result), 200
