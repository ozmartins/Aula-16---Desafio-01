from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

categoria_vacinacao_bp = Blueprint('categoria-vacinacao', __name__)

@categoria_vacinacao_bp.route('/', methods=['GET'])
def listar_categorias_vacinacoes():
    categorias_vacinacoes = select('categoriavacinacao')
    return jsonify([{'co_categoria_vacinacao': r[0], 'no_categoria_vacinacao': r[1]} for r in categorias_vacinacoes])

@categoria_vacinacao_bp.route('/', methods=['POST'])
def criar_categoria_vacinacao():
    data = request.json
    insert('categoriavacinacao', data)
    return jsonify({'mensagem': 'Categoria criada com sucesso'}), 201

@categoria_vacinacao_bp.route('/', methods=['PUT'])
def atualizar_categoria_vacinacao(id):    
    data = request.json
    update('categoriavacinacao', data, f'and co_categoria_vacinacao={id}')
    return jsonify({'mensagem': 'Categoria atualizada com sucesso'})

@categoria_vacinacao_bp.route('/', methods=['DELETE'])
def deletar_categoria_vacinacao(id):
    delete('categoriavacinacao', f'and co_categoria_vacinacao={id}')
    return jsonify({'mensagem': 'Categoria deletada com sucesso'})