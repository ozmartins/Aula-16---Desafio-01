from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

via_administracao_bp = Blueprint('via-administracao', __name__)

@via_administracao_bp.route('/', methods=['GET'])
def listar_vias_administracao():
    vias_administracao = select('viaadministracao')
    return jsonify([{'co_via_administracao': r[0], 'no_via_administracao': r[1]} for r in vias_administracao])

@via_administracao_bp.route('/', methods=['POST'])
def criar_via_administracao():
    data = request.json
    insert('viaadministracao', data)
    return jsonify({'mensagem': 'Via administração criada com sucesso'}), 201

@via_administracao_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_via_administracao(id):    
    data = request.json
    update('viaadministracao', data, f'and co_via_administracao={id}')
    return jsonify({'mensagem': 'Via administração atualizada com sucesso'})

@via_administracao_bp.route('/', methods=['DELETE', 'OPTIONS'])
def deletar_via_administracao(id):
    delete('viaadministracao', f'and co_via_administracao={id}')
    return jsonify({'mensagem': 'Via administração deletada com sucesso'})