from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

uf_bp = Blueprint('uf', __name__)

@uf_bp.route('/', methods=['GET'])
def listar_ufs():
    ufs = select('uf')
    return jsonify([{'co_uf': r[0], 'no_uf': r[1]} for r in ufs])

@uf_bp.route('/', methods=['POST'])
def criar_uf():
    data = request.json
    insert('uf', data)
    return jsonify({'mensagem': 'UF criada com sucesso'}), 201

@uf_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_uf(id):    
    data = request.json
    update('uf', data, f'and co_uf={id}')
    return jsonify({'mensagem': 'UF atualizada com sucesso'})

@uf_bp.route('/', methods=['DELETE'])
def deletar_uf(id):
    delete('uf', f'and co_uf={id}')
    return jsonify({'mensagem': 'UF deletada com sucesso'})