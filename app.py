from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# Ruta para generar las páginas estáticas
@app.route('/generate_static_pages')
def generate_static_pages():
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

        # Genera las páginas estáticas en el directorio 'docs'
        generate_static_html(rows)

        return "Páginas estáticas generadas con éxito."

    except sqlite3.Error as err:
        return f"Error: {err}"

# Función para generar las páginas estáticas
def generate_static_html(rows):
    if not os.path.exists('docs'):
        os.makedirs('docs')

    # Renderiza la plantilla HTML y guarda cada página como un archivo HTML estático
    for row in rows:
        html_content = render_template('static_page_template.html', row=row)

        filename = f"docs/{row[0]}_{row[1]}.html"  # Puedes ajustar el nombre del archivo según tus necesidades
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)

if __name__ == '__main__':
    app.run(debug=True)
