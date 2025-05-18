from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

municipio_bp = Blueprint('municipio', __name__)

@municipio_bp.route('/', methods=['GET'])
def listar_municipios():
    municipios = select('municipio')
    return jsonify([{'co_municipio': r[0], 'no_municipio': r[1]} for r in municipios])

@municipio_bp.route('/', methods=['POST'])
def criar_municipio():
    data = request.json
    insert('municipio', data)
    return jsonify({'mensagem': 'Municipio criado com sucesso'}), 201

@municipio_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_municipio(id):    
    data = request.json
    update('municipio', data, f'and co_municipio={id}')
    return jsonify({'mensagem': 'Municipio atualizado com sucesso'})

@municipio_bp.route('/', methods=['DELETE', 'OPTIONS'])
def deletar_municipio(id):
    delete('municipio', f'and co_municipio={id}')
    return jsonify({'mensagem': 'Municipio deletado com sucesso'})