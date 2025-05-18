from flask import Flask
from flask_cors import CORS
from scripts.db_initializer import initialize_database
from routes.raca import raca_bp    

app = Flask(__name__)
app.register_blueprint(raca_bp, url_prefix='/raca')
CORS(app)

if __name__ == '__main__':
    initialize_database()    
    app.run(debug=True)    
