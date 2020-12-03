import os
import json
from flask import Blueprint, request, jsonify, current_app
from marshmallow.exceptions import ValidationError
from flask_login import login_user, login_required, logout_user
from app.model.tables import User
from app.schemas.serealizer import UserSchema
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email

bp_user = Blueprint('user', __name__)

@bp_user.route('/create_user', methods=['POST'])
def register():
    try:
        us = UserSchema()
        user = us.load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        validate_email(user.email)
    except:
        return jsonify ("Invalid_email"), 400

    users = User.query.filter_by(email=user.email).first()
    if users and users.email == user.email:

        return jsonify("User_alredy_exists"), 400


   # pw_hash = generate_password_hash( user.password.encode('utf-8'), method='pbkdf2:sha512' , salt_length = 8)
   # user.password = pw_hash

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

 
@bp_user.route('/login', methods=["POST"])
def login():

    request_body = request.json

    users = User.query.filter_by(email=request_body['email']).first()

    if users and users.password == request_body['password']:
        
        login_user(users)
        return jsonify({"status": "Logged_in", "user_id": users.id}), 200
    if not users:
        return {"message": "User_missing"}, 404

    if not users.password == request_body['password']:
        return {"message": "Wrong_password"}, 403


@bp_user.route("/logout")
#@login_required
def logout():
    logout_user()
    #return redirect(somewhere)
    return jsonify ("logout efetuado com sucesso!"), 201
