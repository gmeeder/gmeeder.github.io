from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_mensaje', methods=['POST'])
def guardar_mensaje():
    # Obtener los datos del formulario
    nombre = request.form['nombre']
    mensaje = request.form['mensaje']
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Crear el objeto de mensaje
    message_data = {
        'nombre': nombre,
        'mensaje': mensaje,
        'fecha': fecha
    }
    
    # Guardar el mensaje en el archivo JSON
    with open('guestbook.json', 'r+') as file:
        data = json.load(file)
        data.append(message_data)
        file.seek(0)
        json.dump(data, file, indent=4)
    
    # Crear un mensaje de respuesta con un botón para volver al formulario
    response = {
        'message': 'Mensaje guardado correctamente',
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
