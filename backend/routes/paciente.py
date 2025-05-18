from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

paciente_bp = Blueprint('paciente', __name__)

@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
    pacientes = select('paciente')
    return jsonify([{'co_paciente': r[0], 'no_paciente': ''} for r in pacientes])

@paciente_bp.route('/', methods=['POST'])
def criar_paciente():
    data = request.json
    insert('paciente', data)
    return jsonify({'mensagem': 'Paciente criado com sucesso'}), 201

@paciente_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_paciente(id):    
    data = request.json
    update('paciente', data, f'and co_paciente={id}')
    return jsonify({'mensagem': 'Paciente atualizado com sucesso'})

@paciente_bp.route('/', methods=['DELETE'])
def deletar_paciente(id):
    delete('paciente', f'and co_paciente={id}')
    return jsonify({'mensagem': 'Paciente deletado com sucesso'})