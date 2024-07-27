from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler

# Fonction de configuration des logs
def setup_logging():
    # Création d'un handler pour les logs dans un fichier
    file_handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=5)
    file_handler.setLevel(logging.INFO)  # Niveau de logging pour le fichier
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Création d'un handler pour afficher les logs dans la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Niveau de logging pour la console
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # Configuration de la racine du logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

setup_logging()

app = Flask(__name__)
USER_CREDENTIALS = {
    'mokrim': '0000',
    'mohamed': '0000'
}
# Fonction d'addition
def add(a, b):
    return a + b
def authenticate(username, password):
    if USER_CREDENTIALS.get(username) == password:
        return 'Connected'
    else:
        return 'Incorrect username or password'
# Fonction de soustraction
def subtract(a, b):
    return a - b
@app.route('/auth', methods=['POST'])
def auth_route():
    data = request.get_json()
    try:
        username = data.get('username')
        password = data.get('password')
        result=authenticate(username,password)
        logging.info(f"result={result}")
        return jsonify({'result': result}), 200
    except KeyError:
        logging.error("Missing parameters in addition request")
        return jsonify({'error': 'Missing parameters'}), 400
    



    

# Route pour additionner
@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    try:
        a = int(data['a'])  # Convertir en entier
        b = int(data['b'])  # Convertir en entier
        result = add(a, b)
        logging.info(f"Addition request: a={a}, b={b}, result={result}")
        return jsonify({'result': result}), 200
    except KeyError:
        logging.error("Missing parameters in addition request")
        return jsonify({'error': 'Missing parameters'}), 400
    except ValueError:
        logging.error("Invalid input types in addition request")
        return jsonify({'error': 'Invalid input types'}), 400

# Route pour soustraire
@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.get_json()
    try:
        a = int(data['a'])  # Convertir en entier
        b = int(data['b'])
        result = subtract(a, b)
        logging.info(f"Subtraction request: a={a}, b={b}, result={result}")
        return jsonify({'result': result}), 200
    except KeyError:
        logging.error("Missing parameters in subtraction request")
        return jsonify({'error': 'Missing parameters'}), 400
    except ValueError:
        logging.error("Invalid input types in subtraction request")
        return jsonify({'error': 'Invalid input types'}), 400

if __name__ == '__main__':
    app.run()  # Assure-toi de démarrer en mode débogage pour obtenir plus d'informations
