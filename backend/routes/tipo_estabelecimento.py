from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

tipo_estabelecimento_bp = Blueprint('tipo-estabelecimento', __name__)

@tipo_estabelecimento_bp.route('/', methods=['GET'])
def listar_tipos_estabelecimentos():
    tipos_estabelecimentos = select('tipoestabelecimento')
    return jsonify([{'co_tipo_estabelecimento': r[0], 'no_tipo_estabelecimento': r[1]} for r in tipos_estabelecimentos])

@tipo_estabelecimento_bp.route('/', methods=['POST'])
def criar_tipo_estabelecimento():
    data = request.json
    insert('tipoestabelecimento', data)
    return jsonify({'mensagem': 'Tipo estabelecimento criado com sucesso'}), 201

@tipo_estabelecimento_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_tipo_estabelecimento(id):    
    data = request.json
    update('tipoestabelecimento', data, f'and co_tipo_estabelecimento={id}')
    return jsonify({'mensagem': 'Tipo estabelecimento atualizado com sucesso'})

@tipo_estabelecimento_bp.route('/', methods=['DELETE'])
def deletar_tipo_estabelecimento(id):
    delete('tipoestabelecimento', f'and co_tipo_estabelecimento={id}')
    return jsonify({'mensagem': 'Tipo estabelecimento deletado com sucesso'})