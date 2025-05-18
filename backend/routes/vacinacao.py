from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

vacinacao_bp = Blueprint('vacinacao', __name__)

@vacinacao_bp.route('/', methods=['GET'])
def listar_vacinacoes():
    vacinacaos = select('vacinacao')
    return jsonify([{'co_vacinacao': r[0], 'no_vacinacao': r[1]} for r in vacinacaos])

@vacinacao_bp.route('/', methods=['POST'])
def criar_vacinacao():
    data = request.json
    insert('vacinacao', data)
    return jsonify({'mensagem': 'Vacinação criada com sucesso'}), 201

@vacinacao_bp.route('/', methods=['PUT'])
def atualizar_vacinacao(id):    
    data = request.json
    update('vacinacao', data, f'and co_vacinacao={id}')
    return jsonify({'mensagem': 'Vacinação atualizada com sucesso'})

@vacinacao_bp.route('/', methods=['DELETE'])
def deletar_vacinacao(id):
    delete('vacinacao', f'and co_vacinacao={id}')
    return jsonify({'mensagem': 'Vacinação deletada com sucesso'})