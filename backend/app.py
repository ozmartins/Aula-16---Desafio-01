from flask import Flask
from flask_cors import CORS
from scripts.db_initializer import initialize_database
from routes.categoria_vacinacao import categoria_vacinacao_bp
from routes.dose_vacina import dose_vacina_bp
from routes.estabelecimento import estabelecimento_bp
from routes.estrategia_vacinacao import estrategia_vacinacao_bp
from routes.pais import pais_bp
from routes.raca import raca_bp
from routes.etnia_indigena import etnia_indigena_bp
from routes.grupo_atendimento import grupo_atendimento_bp
from routes.local_aplicacao import local_aplicacao_bp
from routes.municipio import municipio_bp
from routes.natureza_estabelecimento import natureza_estabelecimento_bp
from routes.origem_registro import origem_registro_bp
from routes.paciente import paciente_bp
from routes.sistema_origem import sistema_origem_bp
from routes.tipo_estabelecimento import tipo_estabelecimento_bp
from routes.uf import uf_bp
from routes.vacina import vacina_bp
from routes.vacinacao import vacinacao_bp
from routes.vacina_fabricante import vacina_fabricante_bp
from routes.via_administracao import via_administracao_bp

app = Flask(__name__)

app.register_blueprint(categoria_vacinacao_bp, url_prefix='/categoria-vacinacao')
app.register_blueprint(dose_vacina_bp, url_prefix='/dose-vacina')
app.register_blueprint(estabelecimento_bp, url_prefix='/estabelecimento')
app.register_blueprint(estrategia_vacinacao_bp, url_prefix='/estrategia-vacinacao')
app.register_blueprint(etnia_indigena_bp, url_prefix='/etnia-indigena')
app.register_blueprint(vacina_fabricante_bp, url_prefix='/vacina-fabricante')
app.register_blueprint(grupo_atendimento_bp, url_prefix='/grupo-atendimento')
app.register_blueprint(local_aplicacao_bp, url_prefix='/local-aplicacao')
app.register_blueprint(municipio_bp, url_prefix='/municipio')
app.register_blueprint(natureza_estabelecimento_bp, url_prefix='/natureza-estabelecimento')
app.register_blueprint(origem_registro_bp, url_prefix='/origem-registro')
app.register_blueprint(paciente_bp, url_prefix='/paciente')
app.register_blueprint(pais_bp, url_prefix='/pais')
app.register_blueprint(raca_bp, url_prefix='/raca')
app.register_blueprint(sistema_origem_bp, url_prefix='/sistema-origem')
app.register_blueprint(tipo_estabelecimento_bp, url_prefix='/tipo-estabelecimento')
app.register_blueprint(uf_bp, url_prefix='/uf')
app.register_blueprint(vacina_bp, url_prefix='/vacina')
app.register_blueprint(vacinacao_bp, url_prefix='/vacinacao')
app.register_blueprint(via_administracao_bp, url_prefix='/via-administracao')

CORS(app)

if __name__ == '__main__':
    initialize_database()    
    app.run(debug=True)    
