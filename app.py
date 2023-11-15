from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    try:
        # Conéctate a la base de datos SQLite
        connection = sqlite3.connect('datosterrenodb.sqlite')
        cursor = connection.cursor()

        # Ejecuta una consulta SELECT para obtener los datos de la tabla
        cursor.execute("SELECT * FROM ContingenciaCair")

        # Obtiene todos los resultados
        rows = cursor.fetchall()

        # Cierra la conexión
        connection.close()

        # Renderiza la plantilla HTML y pasa los datos a la página
        return render_template('index.html', rows=rows)

    except sqlite3.Error as err:
        return f"Error: {err}"

if __name__ == '__main__':
    app.run(debug=True)
