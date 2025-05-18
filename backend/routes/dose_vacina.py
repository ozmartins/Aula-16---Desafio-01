from flask import  request, jsonify, Blueprint
from scripts.db_manager import insert, update, delete, select

dose_vacina_bp = Blueprint('dose-vacina', __name__)

@dose_vacina_bp.route('/', methods=['GET'])
def listar_doses_vacinas():
    doses_vacinas = select('dosevacina')
    return jsonify([{'co_dose_vacina': r[0], 'no_dose_vacina': r[1]} for r in doses_vacinas])

@dose_vacina_bp.route('/', methods=['POST'])
def criar_dose_vacina():
    data = request.json
    insert('dosevacina', data)
    return jsonify({'mensagem': 'Dose criada com sucesso'}), 201

@dose_vacina_bp.route('/', methods=['PUT', 'OPTIONS'])
def atualizar_dose_vacina(id):    
    data = request.json
    update('dosevacina', data, f'and co_dose_vacina={id}')
    return jsonify({'mensagem': 'Dose atualizada com sucesso'})

@dose_vacina_bp.route('/', methods=['DELETE'])
def deletar_dose_vacina(id):
    delete('dosevacina', f'and co_dose_vacina={id}')
    return jsonify({'mensagem': 'Dose deletada com sucesso'})