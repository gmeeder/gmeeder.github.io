from flask import Flask, render_template, request, redirect, url_for
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Recopilar datos del formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    dni = request.form['dni']
    localidad = request.form['localidad']
    
    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)  # Cambiar "Arial" por "Helvetica"
    pdf.cell(200, 10, txt="Información de la Persona", ln=True, align='C')
    pdf.cell(200, 10, txt="", ln=True, align='C') # Nueva línea
    pdf.cell(200, 10, txt=f"Nombre: {nombre}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Apellido: {apellido}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Edad: {edad}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"DNI: {dni}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Localidad: {localidad}", ln=True, align='L')
    
    pdf_output = f"static/{nombre}_{apellido}_info.pdf"
    
    # Crear directorio si no existe
    os.makedirs(os.path.dirname(pdf_output), exist_ok=True)
    
    pdf.output(pdf_output)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
