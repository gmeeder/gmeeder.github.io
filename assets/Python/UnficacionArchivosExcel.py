import pandas as pd

# Lee los archivos Excel
Enero_CierreMes = pd.read_excel("Enero_CierreMes.xlsx")
Febrero_CierreMes = pd.read_excel("Febrero_CierreMes.xlsx")
Marzo_CierreMes = pd.read_excel("Marzo_CierreMes.xlsx")
Abril_CierreMes = pd.read_excel("Abril_CierreMes.xlsx")

# Agrega una columna para indicar el nombre del archivo original
Enero_CierreMes['Nombre_archivo'] = 'Enero_CierreMes'
Febrero_CierreMes['Nombre_archivo'] = 'Febrero_CierreMes'
Marzo_CierreMes['Nombre_archivo'] = 'Marzo_CierreMes'
Abril_CierreMes['Nombre_archivo'] = 'Abril_CierreMes'

# Combina los DataFrames en uno solo
merged_data = pd.concat([Enero_CierreMes, Febrero_CierreMes, Marzo_CierreMes, Abril_CierreMes])

# Guarda el DataFrame combinado en un nuevo archivo Excel
merged_data.to_excel("datos_combinados.xlsx", index=False)