from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

estrategia_vacinacao_bp = Blueprint('estrategia-vacinacao', __name__)

@estrategia_vacinacao_bp.route('/', methods=['GET'])
def listar_estrategias_vacinacoes():
    estrategias_vacinacaos = select('estrategiavacinacao')
    return jsonify([{'co_estrategia_vacinacao': r[0], 'no_estrategia_vacinacao': r[1]} for r in estrategias_vacinacaos])

@estrategia_vacinacao_bp.route('/', methods=['POST'])
def criar_estrategia_vacinacao():
    data = request.json
    insert('estrategiavacinacao', data)
    return jsonify({'mensagem': 'Estratégia criada com sucesso'}), 201

@estrategia_vacinacao_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_estrategia_vacinacao(id):    
    data = request.json
    update('estrategiavacinacao', data, f'and co_estrategia_vacinacao={id}')
    return jsonify({'mensagem': 'Estratégia atualizada com sucesso'})

@estrategia_vacinacao_bp.route('/', methods=['DELETE', 'OPTIONS'])
def deletar_estrategia_vacinacao(id):
    delete('estrategiavacinacao', f'and co_estrategia_vacinacao={id}')
    return jsonify({'mensagem': 'Estratégia deletada com sucesso'})