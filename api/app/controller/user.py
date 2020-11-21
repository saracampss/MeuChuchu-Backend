from flask import Blueprint, request, jsonify, current_app
from app.model.tables import User
from app.schemas.serealizer import UserSchema

bp_user = Blueprint('user', __name__)
@bp_user.route('/mostrar', methods=['GET'])
def mostrar():
    result = User.query.all()
    return UserSchema(many=True).jsonify(result), 200

@bp_user.route('/create-user', methods=['POST'])
def register():
    us = UserSchema()

    user = us.load(request.json)

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return us.jsonify(user), 201

#@bp_user.route('/create-user', methods=['POST'])
#def register():
#    us = UserSchema()
#
#    user, error = us.load(request.json)
#
#    if error:
#        return jsonify(error), 401
#
#    user.gen_hash()
#
#    current_app.db.session.add(user)
#    current_app.db.session.commit()
#
#    return us.jsonify(user), 201