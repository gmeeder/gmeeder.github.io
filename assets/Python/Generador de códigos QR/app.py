from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form['url']
    qr = qrcode.make(url)
    qr.save('static/qrcode.png')
    return render_template('result.html', url=url)

if __name__ == '__main__':
    app.run(debug=True)
