from flask import Flask
from flask_cors import CORS
from scripts.db_initializer import initialize_database
from routes.raca import raca_bp
from routes.pais import pais_bp
from routes.etnia_indigena import etnia_indigena_bp

app = Flask(__name__)
app.register_blueprint(raca_bp, url_prefix='/raca')
app.register_blueprint(pais_bp, url_prefix='/pais')
app.register_blueprint(etnia_indigena_bp, url_prefix='/etnia-indigena')
CORS(app)

if __name__ == '__main__':
    initialize_database()    
    app.run(debug=True)    
