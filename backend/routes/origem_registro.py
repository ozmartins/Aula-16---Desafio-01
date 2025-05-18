from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

origem_registro_bp = Blueprint('origem-registro', __name__)

@origem_registro_bp.route('/', methods=['GET'])
def listar_origens_registros():
    origens_registros = select('origemregistro')
    return jsonify([{'co_origem_registro': r[0], 'no_origem_registro': r[1]} for r in origens_registros])

@origem_registro_bp.route('/', methods=['POST'])
def criar_origem_registro():
    data = request.json
    insert('origemregistro', data)
    return jsonify({'mensagem': 'Origem do registro criada com sucesso'}), 201

@origem_registro_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_origem_registro(id):    
    data = request.json
    update('origemregistro', data, f'and co_origem_registro={id}')
    return jsonify({'mensagem': 'Origem do registro atualizada com sucesso'})

@origem_registro_bp.route('/', methods=['DELETE'])
def deletar_origem_registro(id):
    delete('origemregistro', f'and co_origem_registro={id}')
    return jsonify({'mensagem': 'Origem do registro deletada com sucesso'})