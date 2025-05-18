from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

raca_bp = Blueprint('raca', __name__)

@raca_bp.route('/', methods=['GET'])
def listar_racas():
    racas = select('raca')
    return jsonify([{'co_raca_cor': r[0], 'no_raca_cor': r[1]} for r in racas])

@raca_bp.route('/', methods=['POST'])
def criar_raca():
    data = request.json
    insert('raca', data)
    return jsonify({'mensagem': 'Raça criada com sucesso'}), 201

@raca_bp.route('/', methods=['PUT'])
def atualizar_raca(id):    
    data = request.json
    update('raca', data, f'and co_raca_cor={id}')
    return jsonify({'mensagem': 'Raça atualizada com sucesso'})

@raca_bp.route('/', methods=['DELETE'])
def deletar_raca(id):
    delete('raca', f'and co_raca_cor={id}')
    return jsonify({'mensagem': 'Raça deletada com sucesso'})