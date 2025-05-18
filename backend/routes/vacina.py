from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

vacina_bp = Blueprint('vacina', __name__)

@vacina_bp.route('/', methods=['GET'])
def listar_vacinas():
    vacinas = select('vacina')
    return jsonify([{'co_vacina': r[0], 'no_vacina': r[1]} for r in vacinas])

@vacina_bp.route('/', methods=['POST'])
def criar_vacina():
    data = request.json
    insert('vacina', data)
    return jsonify({'mensagem': 'Vacina criada com sucesso'}), 201

@vacina_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_vacina(id):    
    data = request.json
    update('vacina', data, f'and co_vacina={id}')
    return jsonify({'mensagem': 'Vacina atualizada com sucesso'})

@vacina_bp.route('/', methods=['DELETE', 'OPTIONS'])
def deletar_vacina(id):
    delete('vacina', f'and co_vacina={id}')
    return jsonify({'mensagem': 'Vacina deletada com sucesso'})