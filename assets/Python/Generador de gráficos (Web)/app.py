from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Datos de inflación para España
inflacion_espana = {
    'Año': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Inflación_media_anual_ES': [2.3, 2.1, 3, 3.6, 4.1, 4, -0.3, 1.5, 2.9, 2.8, 0.3, -0.5, 0, 0.2, 1.2, 1.1, 0.5, 0.5, 5.9, 8.4, 5.4]
}

# Datos de inflación para Francia
inflacion_francia = {
    'Año': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Inflación_media_anual_FR': [1.8, 1.7, 1.8, 1.5, 1.8, 3.2, 0.1, 1.5, 2.1, 1.9, 0.8, 0, 0.1, 0.3, 1, 2.1, 1.3, 0.5, 1.8, 2.9, 2.5]
}

# Datos de inflación para Alemania
inflacion_alemania = {
    'Año': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Inflación_media_anual_DE': [1.1, 1.6, 1.9, 1.8, 2.3, 2.6, 0.2, 1.1, 2.5, 2.1, 1.5, 0.9, 0.1, 0.5, 1.5, 1.8, 1.4, 0.5, 2.1, 3.5, 2.9]
}

# Datos de inflación para Italia
inflacion_italia = {
    'Año': [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Inflación_media_anual_IT': [2.9, 2.3, 2.2, 2.2, 2.1, 3.3, 0.8, 1.6, 2.8, 2.4, 1.2, 0.2, 0, 0.1, 1.1, 1.4, 0.6, 0.3, 2.1, 3.7, 3.2]
}

# Convertir a DataFrames de Pandas
df_espana = pd.DataFrame(inflacion_espana)
df_francia = pd.DataFrame(inflacion_francia)
df_alemania = pd.DataFrame(inflacion_alemania)
df_italia = pd.DataFrame(inflacion_italia)

@app.route('/')
def index():
    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(df_espana['Año'], df_espana['Inflación_media_anual_ES'], marker='o', linestyle='-', label='España')
    plt.plot(df_francia['Año'], df_francia['Inflación_media_anual_FR'], marker='o', linestyle='-', label='Francia')
    plt.plot(df_alemania['Año'], df_alemania['Inflación_media_anual_DE'], marker='o', linestyle='-', label='Alemania')
    plt.plot(df_italia['Año'], df_italia['Inflación_media_anual_IT'], marker='o', linestyle='-', label='Italia')
    plt.title('Inflación Media Anual en Países Europeos (2003-2023)')
    plt.xlabel('Año')
    plt.ylabel('Inflación Media Anual (%)')
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico en un buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    buffer_encoded = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Renderizar la plantilla con el gráfico incrustado
    return render_template('index.html', plot=buffer_encoded)

if __name__ == '__main__':
    app.run(debug=True)
