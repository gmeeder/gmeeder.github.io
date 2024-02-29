from flask import Flask, render_template, request
import os
import speech_recognition as sr

app = Flask(__name__)

# Ruta del directorio donde se guardarán los archivos de audio subidos
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Función para convertir audio a texto
def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="es-ES")
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Comprobamos si se ha subido un archivo
        if 'file' not in request.files:
            return render_template('index.html', error='No se ha seleccionado ningún archivo')
        
        file = request.files['file']
        
        # Comprobamos si se ha subido un archivo válido
        if file.filename == '':
            return render_template('index.html', error='No se ha seleccionado ningún archivo')
        
        # Guardamos el archivo en el directorio de uploads
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        # Convertimos el audio a texto
        audio_text = convert_audio_to_text(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        # Eliminamos el archivo subido
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        
        return render_template('index.html', audio_text=audio_text)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
