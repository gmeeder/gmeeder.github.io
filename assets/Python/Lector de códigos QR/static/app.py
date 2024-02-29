from flask import Flask, render_template, Response
import cv2
from pyzbar.pyzbar import decode
import threading

app = Flask(__name__)

# Objeto para bloquear el acceso al frame de vídeo
lock = threading.Lock()

# Inicializar la cámara web
camera = cv2.VideoCapture(0)

# Función para capturar y transmitir vídeo
def video_stream():
    global camera
    while True:
        success, frame = camera.read()
        if not success:
            print("No se puede obtener el fotograma de la cámara.")
            break

        # Detección de códigos QR
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            # Superposición de texto en el vídeo
            cv2.putText(frame, str(obj.data.decode('utf-8')), (obj.rect.left, obj.rect.top),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Ruta para el streaming de vídeo
@app.route('/video_feed')
def video_feed():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
