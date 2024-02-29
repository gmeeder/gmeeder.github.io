from flask import Flask, render_template, request, jsonify
import pyttsx3
import threading

app = Flask(__name__)

def convertir_texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidad de habla
    engine.say(texto)
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convertir', methods=['POST'])
def convertir():
    texto = request.form['texto']
    # Ejecutar la conversión en un hilo paralelo
    t = threading.Thread(target=convertir_texto_a_voz, args=(texto,))
    t.start()
    return jsonify({'mensaje': 'La conversión está en proceso'})

if __name__ == '__main__':
    app.run(debug=True)
