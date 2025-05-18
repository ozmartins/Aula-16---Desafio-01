from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

pais_bp = Blueprint('pais', __name__)

@pais_bp.route('/', methods=['GET'])
def listar_paises():
    paises = select('pais')
    return jsonify([{'co_pais': r[0], 'no_pais': r[1]} for r in paises])

@pais_bp.route('/', methods=['POST'])
def criar_pais():
    data = request.json
    insert('pais', data)
    return jsonify({'mensagem': 'País criado com sucesso'}), 201

@pais_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_pais(id):    
    data = request.json
    update('pais', data, f'and co_pais={id}')
    return jsonify({'mensagem': 'País atualizado com sucesso'})

@pais_bp.route('/', methods=['DELETE'])
def deletar_pais(id):
    delete('pais', f'and co_pais={id}')
    return jsonify({'mensagem': 'País deletado com sucesso'})