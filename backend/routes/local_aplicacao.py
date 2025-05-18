from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

local_aplicacao_bp = Blueprint('local-aplicacao', __name__)

@local_aplicacao_bp.route('/', methods=['GET'])
def listar_locais_aplicacoes():
    locais_aplicacoes = select('localaplicacao')
    return jsonify([{'co_local_aplicacao': r[0], 'no_local_aplicacao': r[1]} for r in locais_aplicacoes])

@local_aplicacao_bp.route('/', methods=['POST'])
def criar_local_aplicacao():
    data = request.json
    insert('localaplicacao', data)
    return jsonify({'mensagem': 'Local aplicação criado com sucesso'}), 201

@local_aplicacao_bp.route('/', methods=['PUT'])
def atualizar_local_aplicacao(id):    
    data = request.json
    update('localaplicacao', data, f'and co_local_aplicacao={id}')
    return jsonify({'mensagem': 'Local aplicação atualizado com sucesso'})

@local_aplicacao_bp.route('/', methods=['DELETE'])
def deletar_local_aplicacao(id):
    delete('localaplicacao', f'and co_local_aplicacao={id}')
    return jsonify({'mensagem': 'Local aplicação deletado com sucesso'})