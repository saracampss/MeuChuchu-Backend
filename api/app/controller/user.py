from flask import Blueprint, request, jsonify, current_app
from app.model.tables import User
from app.schemas.serealizer import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash

bp_user = Blueprint('user', __name__)

@bp_user.route('/create-user', methods=['POST'])
def register():
    us = UserSchema()

    user = us.load(request.json)

    pw_hash = generate_password_hash( user.password.encode('utf-8'), method='pbkdf2:sha512' , salt_length = 8)
    user.password = pw_hash


    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201

@bp_user.route('/mostrar', methods=['GET'])
def mostrar():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200

@bp_user.route('/modificar_user/<identificador>',methods=['POST'])
def modificar(identificador):
    bs = UserSchema()
    query = User.query.filter(User.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_user.route('/delete_user/<identificador>', methods=['GET'])
def deletar(identificador):
    User.query.filter(User.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!')
