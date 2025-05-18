from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

natureza_estabelecimento_bp = Blueprint('natureza-estabelecimento', __name__)

@natureza_estabelecimento_bp.route('/', methods=['GET'])
def listar_naturezas_estabelecimentos():
    naturezas_estabelecimentos = select('naturezaestabelecimento')
    return jsonify([{'co_natureza_estabelecimento': r[0], 'no_natureza_estabelecimento': r[1]} for r in naturezas_estabelecimentos])

@natureza_estabelecimento_bp.route('/', methods=['POST'])
def criar_natureza_estabelecimento():
    data = request.json
    insert('naturezaestabelecimento', data)
    return jsonify({'mensagem': 'Natureza estabelecimento criada com sucesso'}), 201

@natureza_estabelecimento_bp.route('/', methods=['PUT'])
def atualizar_natureza_estabelecimento(id):    
    data = request.json
    update('naturezaestabelecimento', data, f'and co_natureza_estabelecimento={id}')
    return jsonify({'mensagem': 'Natureza estabelecimento atualizada com sucesso'})

@natureza_estabelecimento_bp.route('/', methods=['DELETE'])
def deletar_natureza_estabelecimento(id):
    delete('naturezaestabelecimento', f'and co_natureza_estabelecimento={id}')
    return jsonify({'mensagem': 'Natureza estabelecimento deletada com sucesso'})