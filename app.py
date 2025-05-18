from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from scripts.db_manager import insert, update, delete, select
from scripts.db_initializer import initialize_database

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Vacinacao.db'

db = SQLAlchemy(app)

class Raca(db.Model):
    co_raca_cor = db.Column(db.Integer, primary_key=True)
    no_raca_cor = db.Column(db.String(100), nullable=False)

@app.route('/racas', methods=['GET'])
def listar_racas():
    racas = select('raca')
    return jsonify([{'co_raca_cor': r[0], 'no_raca_cor': r[1]} for r in racas])

@app.route('/racas', methods=['POST'])
def criar_raca():
    data = request.json
    nova_raca = Raca(no_raca_cor=data['no_raca_cor'])
    db.session.add(nova_raca)
    db.session.commit()
    return jsonify({'mensagem': 'Raca criada com sucesso'}), 201

@app.route('/racas/<int:id>', methods=['PUT'])
def atualizar_raca(id):
    raca = Raca.query.get_or_404(id)
    data = request.json
    raca.no_raca_cor = data['no_raca_cor']
    db.session.commit()
    return jsonify({'mensagem': 'Raca atualizada com sucesso'})

@app.route('/racas/<int:id>', methods=['DELETE'])
def deletar_raca(id):
    raca = Raca.query.get_or_404(id)
    db.session.delete(raca)
    db.session.commit()
    return jsonify({'mensagem': 'Raca deletada com sucesso'})

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
