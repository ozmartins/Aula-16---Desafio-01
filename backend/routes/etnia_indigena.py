from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

etnia_indigena_bp = Blueprint('etnia-indigena', __name__)

@etnia_indigena_bp.route('/', methods=['GET'])
def listar_etnias_indigenas():
    etnias_indigenas = select('etniaindigena')
    return jsonify([{'co_etnia_indigena': r[0], 'no_etnia_indigena': r[1]} for r in etnias_indigenas])

@etnia_indigena_bp.route('/', methods=['POST'])
def criar_etnia_indigena():
    data = request.json
    insert('etniaindigena', data)
    return jsonify({'mensagem': 'Etnia indígena criada com sucesso'}), 201

@etnia_indigena_bp.route('/', methods=['PUT'])
def atualizar_etnia_indigena(id):    
    data = request.json
    update('etnia_indigena', data, f'and co_etnia_indigena={id}')
    return jsonify({'mensagem': 'Etnia indígena atualizada com sucesso'})

@etnia_indigena_bp.route('/', methods=['DELETE'])
def deletar_etnia_indigena(id):
    delete('etnia_indigena', f'and co_etnia_indigena={id}')
    return jsonify({'mensagem': 'Etnia indígena deletada com sucesso'})