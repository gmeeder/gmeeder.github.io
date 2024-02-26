from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Función para realizar la conversión de divisas utilizando la API de APILayer
def convertir_divisas(cantidad, moneda_origen, moneda_destino):
    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": cantidad,
        "from": moneda_origen,
        "to": moneda_destino
    }
    headers = {"apikey": "mpkdbrzjDedAgWv8eSgowXmIwghcTcjc"}

    response = requests.get(url, headers=headers, params=payload)
    if response.status_code == 200:
        data = response.json()
        return data['result']
    else:
        return "Error en la solicitud de conversión de divisas"

# Ruta principal para mostrar el formulario y los resultados
@app.route('/', methods=['GET', 'POST'])
def conversor():
    # Lista de opciones de moneda
    monedas = ['EUR', 'USD', 'CNY', 'JPY']
    
    if request.method == 'POST':
        cantidad = float(request.form['cantidad'])
        moneda_origen = request.form['moneda_origen']
        moneda_destino = request.form['moneda_destino']

        # Realizar la conversión de divisas
        resultado = convertir_divisas(cantidad, moneda_origen, moneda_destino)

        return render_template('index.html', monedas=monedas, resultado=resultado)
    
    return render_template('index.html', monedas=monedas)

if __name__ == '__main__':
    app.run(debug=True)
