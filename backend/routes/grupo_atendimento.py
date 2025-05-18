from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

grupo_atendimento_bp = Blueprint('grupo-atendimento', __name__)

@grupo_atendimento_bp.route('/', methods=['GET'])
def listar_grupos_atendimentos():
    grupos_atendimentos = select('grupoatendimento')
    return jsonify([{'co_grupo_atendimento': r[0], 'no_grupo_atendimento': r[1]} for r in grupos_atendimentos])

@grupo_atendimento_bp.route('/', methods=['POST'])
def criar_grupo_atendimento():
    data = request.json
    insert('grupoatendimento', data)
    return jsonify({'mensagem': 'Grupo atendimento criado com sucesso'}), 201

@grupo_atendimento_bp.route('/', methods=['PUT'])
def atualizar_grupo_atendimento(id):    
    data = request.json
    update('grupoatendimento', data, f'and co_grupo_atendimento={id}')
    return jsonify({'mensagem': 'Grupo atendimento atualizado com sucesso'})

@grupo_atendimento_bp.route('/', methods=['DELETE'])
def deletar_grupo_atendimento(id):
    delete('grupoatendimento', f'and co_grupo_atendimento={id}')
    return jsonify({'mensagem': 'Grupo atendimento deletado com sucesso'})