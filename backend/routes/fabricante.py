from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

fabricante_bp = Blueprint('fabricante', __name__)

@fabricante_bp.route('/', methods=['GET'])
def listar_fabricantes():
    fabricantes = select('fabricante')
    return jsonify([{'co_fabricante': r[0], 'no_fabricante': r[1]} for r in fabricantes])

@fabricante_bp.route('/', methods=['POST'])
def criar_fabricante():
    data = request.json
    insert('fabricante', data)
    return jsonify({'mensagem': 'Fabricante criado com sucesso'}), 201

@fabricante_bp.route('/', methods=['PUT'])
def atualizar_fabricante(id):    
    data = request.json
    update('fabricante', data, f'and co_fabricante={id}')
    return jsonify({'mensagem': 'Fabricante atualizado com sucesso'})

@fabricante_bp.route('/', methods=['DELETE'])
def deletar_fabricante(id):
    delete('fabricante', f'and co_fabricante={id}')
    return jsonify({'mensagem': 'Fabricante deletado com sucesso'})