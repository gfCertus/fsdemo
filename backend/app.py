from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def cargar_usuarios():
    try:
        with open('usuarios.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

usuarios = cargar_usuarios()

@app.route('/hola', methods=['GET'])
def hola():
    return jsonify({'mensaje': '¡Hola desde el backend de Flask!'})

@app.route('/usuario', methods=['POST'])
def usuario():
    data = request.get_json()
    nomUsuario = data.get('usuario')
    password = data.get('password')

    # Lógica de autenticación
    if nomUsuario in usuarios and usuarios[nomUsuario]['password'] == password:
        return jsonify({
            'nomUsuario': nomUsuario,
            'nombre': usuarios[nomUsuario]['nombre'],
            'apellido': usuarios[nomUsuario]['apellido'],
            'status': usuarios[nomUsuario]['status'],
            'rol': usuarios[nomUsuario]['rol']
        })
    else:
        return jsonify({'mensaje': 'Usuario o contraseña incorrectos'}), 401 # 401 Unauthorized

if __name__ == '__main__':
    app.run(debug=True)