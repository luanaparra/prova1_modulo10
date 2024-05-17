from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, jwt_required, unset_jwt_cookies, get_jwt_identity
from .models import User, Task
from . import db

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, Murilo, odeio prova!'})

@api_bp.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 409
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@api_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        response = jsonify({'login': True})
        set_access_cookies(response, access_token)
        return response
    return jsonify({'login': False}), 401

@api_bp.route('/pedidos', methods=['GET', 'POST'])
@jwt_required()
def pedidos():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        novo = request.json.get('novo')
        pedido = Pedido(novo=novo, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Novo pedido adicionado'}), 201
    else:
        pedidos = Pedido.query.filter_by(user_id=user_id).all()
        return jsonify({'pedidos': [{'id': pedido.id, 'title': pedido.novo, 'completed': pedido.completed} for pedido in pedidos]})
    

@api_bp.route('/pedidos/<int:id>/complete', methods=['PUT'])
@jwt_required()
def complete_pedido(id):
    user_id = get_jwt_identity()
    pedido = Pedido.query.filter_by(id=id, user_id=user_id).first()
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    pedido.completed = True
    db.session.commit()
    return jsonify({'message': 'Pedido encontrado com sucesso.'})

@api_bp.route('/pedidos/<int:id>', methods=['DELETE']) 
@jwt_required()
def delete_pedido(id):
    user_id = get_jwt_identity()
    pedido = Pedido.query.filter_by(id=id, user_id=user_id).first()
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    db.session.delete(pedido)
    db.session.commit()
    return jsonify({'message': 'Pedido deletado com sucesso.'})

@api_bp.route('/pedidos/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    user_id = get_jwt_identity()
    pedido = Pedido.query.filter_by(id=id, user_id=user_id).first()
    if not pedido:
        return jsonify({'message': 'Pedido não encontrado'}), 404
    novo = request.json.get('novo')
    pedido.novo = novo
    db.session.commit()
    return jsonify({'message': 'Pedido editado com sucesso.'})
