from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

categoria_atendimento_bp = Blueprint('categoria-atendimento', __name__)

@categoria_atendimento_bp.route('/', methods=['GET'])
def listar_categorias_vacinacoes():
    categorias_vacinacoes = select('categoriaatendimento')
    return jsonify([{'co_vacina_categoria_atendimento': r[0], 'no_vacina_categoria_atendimento': r[1]} for r in categorias_vacinacoes])

@categoria_atendimento_bp.route('/', methods=['POST'])
def criar_categoria_atendimento():
    data = request.json
    insert('categoriaatendimento', data)
    return jsonify({'mensagem': 'Categoria criada com sucesso'}), 201

@categoria_atendimento_bp.route('/', methods=['PUT'])
def atualizar_categoria_atendimento(id):    
    data = request.json
    update('categoriaatendimento', data, f'and co_vacina_categoria_atendimento={id}')
    return jsonify({'mensagem': 'Categoria atualizada com sucesso'})

@categoria_atendimento_bp.route('/', methods=['DELETE'])
def deletar_categoria_atendimento(id):
    delete('categoriaatendimento', f'and co_vacina_categoria_atendimento={id}')
    return jsonify({'mensagem': 'Categoria deletada com sucesso'})