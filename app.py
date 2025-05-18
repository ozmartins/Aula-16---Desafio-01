from flask import Flask, request, jsonify
from flask_cors import CORS
from scripts.db_manager import insert, update, delete, select
from scripts.db_initializer import initialize_database

app = Flask(__name__)

CORS(app)

@app.route('/racas', methods=['GET'])
def listar_racas():
    racas = select('raca')
    return jsonify([{'co_raca_cor': r[0], 'no_raca_cor': r[1]} for r in racas])

@app.route('/racas', methods=['POST'])
def criar_raca():
    data = request.json
    insert('raca', data)
    return jsonify({'mensagem': 'Raca criada com sucesso'}), 201

@app.route('/racas/<int:id>', methods=['PUT'])
def atualizar_raca(id):    
    data = request.json
    update('raca', data, f'and co_raca_cor={id}')
    return jsonify({'mensagem': 'Raca atualizada com sucesso'})

@app.route('/racas/<int:id>', methods=['DELETE'])
def deletar_raca(id):
    delete('raca', f'and co_raca_cor={id}')
    return jsonify({'mensagem': 'Raca deletada com sucesso'})

if __name__ == '__main__':
    initialize_database()    
    app.run(debug=True)
