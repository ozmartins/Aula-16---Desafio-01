from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

vacina_fabricante_bp = Blueprint('vacina-fabricante', __name__)

@vacina_fabricante_bp.route('/', methods=['GET'])
def listar_fabricantes():
    vacina_fabricantes = select('vacinafabricante')
    return jsonify([{'co_vacina_fabricante': r[0], 'no_vacina_fabricante': r[1]} for r in vacina_fabricantes])

@vacina_fabricante_bp.route('/', methods=['POST'])
def criar_fabricante():
    data = request.json
    insert('vacinafabricante', data)
    return jsonify({'mensagem': 'Fabricante criado com sucesso'}), 201

@vacina_fabricante_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_fabricante(id):    
    data = request.json
    update('vacinafabricante', data, f'and co_vacina_fabricante={id}')
    return jsonify({'mensagem': 'Fabricante atualizado com sucesso'})

@vacina_fabricante_bp.route('/', methods=['DELETE'])
def deletar_fabricante(id):
    delete('vacinafabricante', f'and co_vacina_fabricante={id}')
    return jsonify({'mensagem': 'Fabricante deletado com sucesso'})