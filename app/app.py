from flask import Flask, request, jsonify

app = Flask(__name__)

# Fonction d'addition
def add(a, b):
    return a + b

# Fonction de soustraction
def subtract(a, b):
    return a - b

# Route pour additionner
@app.route('/add', methods=['POST'])
def add_route():
    data = request.get_json()
    try:
        a = int(data['a'])  # Convertir en entier
        b = int(data['b'])  # Convertir en entier
        result = add(a, b)
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Missing parameters'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid input types'}), 400

# Route pour soustraire
@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.get_json()
    try:
        a = int(data['a'])  # Convertir en entier
        b = int(data['b'])  
        result = subtract(a, b)
        return jsonify({'result': result}), 200
    except KeyError:
        return jsonify({'error': 'Missing parameters'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid input types'}), 400

if __name__ == '__main__':
    app.run()
