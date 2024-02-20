import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos proporcionados
data = {
    'Mes': ['Ene 2023', 'Feb 2023', 'Mar 2023', 'Abr 2023', 'May 2023', 'Jun 2023',
            'Jul 2023', 'Ago 2023', 'Sep 2023', 'Oct 2023', 'Nov 2023', 'Dic 2023'],
    'Cantidad': [2324, 3230, 4588, 18731, 4021, 14687, 4837, 19100, 13725, 22368, 10574, 14449]
}
df = pd.DataFrame(data)

# Mostrar estadísticas descriptivas básicas
print(df.describe())

# Visualización: Gráfico de línea para mostrar la tendencia temporal
plt.figure(figsize=(10, 6))
plt.plot(df['Mes'], df['Cantidad'], marker='o')
plt.title('Cantidad por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# count: Número de observaciones en el DataFrame (en este caso, 12 meses)
# mean: Media de las cantidades vendidas a lo largo de los meses
# std: Desviación estándar de las cantidades vendidas
# min: Valor mínimo de las cantidades vendidas
# 25%: Primer cuartil, indica el valor por debajo del cual se encuentra el 25% de los datos
# 50%: Mediana, valor que separa la mitad más baja de la mitad más alta de los datos
# 75%: Tercer cuartil, indica el valor por debajo del cual se encuentra el 75% de los datos
# max: Valor máximo de las cantidades vendidas
