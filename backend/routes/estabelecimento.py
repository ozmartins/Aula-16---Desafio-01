from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

estabelecimento_bp = Blueprint('estabelecimento', __name__)

@estabelecimento_bp.route('/', methods=['GET'])
def listar_estabelecimentos():
    estabelecimentos = select('estabelecimento')
    return jsonify([{'co_estabelecimento': r[0], 'no_estabelecimento': r[1]} for r in estabelecimentos])

@estabelecimento_bp.route('/', methods=['POST'])
def criar_estabelecimento():
    data = request.json
    insert('estabelecimento', data)
    return jsonify({'mensagem': 'Estabecimento criado com sucesso'}), 201

@estabelecimento_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_estabelecimento(id):    
    data = request.json
    update('estabelecimento', data, f'and co_estabelecimento={id}')
    return jsonify({'mensagem': 'Estabecimento atualizado com sucesso'})

@estabelecimento_bp.route('/', methods=['DELETE'])
def deletar_estabelecimento(id):
    delete('estabelecimento', f'and co_estabelecimento={id}')
    return jsonify({'mensagem': 'Estabecimento deletado com sucesso'})