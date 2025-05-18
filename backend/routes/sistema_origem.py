from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

sistema_origem_bp = Blueprint('sistema-origem', __name__)

@sistema_origem_bp.route('/', methods=['GET'])
def listar_sistemas_origens():
    sistemas_origem = select('sistemaorigem')
    return jsonify([{'co_sistema_origem': r[0], 'no_sistema_origem': r[1]} for r in sistemas_origem])

@sistema_origem_bp.route('/', methods=['POST'])
def criar_sistema_origem():
    data = request.json
    insert('sistemaorigem', data)
    return jsonify({'mensagem': 'Sistema origem criado com sucesso'}), 201

@sistema_origem_bp.route('/', methods=['PUT'])
def atualizar_sistema_origem(id):    
    data = request.json
    update('sistemaorigem', data, f'and co_sistema_origem={id}')
    return jsonify({'mensagem': 'Sistema origem atualizado com sucesso'})

@sistema_origem_bp.route('/', methods=['DELETE'])
def deletar_sistema_origem(id):
    delete('sistemaorigem', f'and co_sistema_origem={id}')
    return jsonify({'mensagem': 'Sistema origem deletado com sucesso'})