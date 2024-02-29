# resultado como entero
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de entrada (meses)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16],[17],[18],[19],[20],[21],[22]]) #Repas terreno: enero 2022 a abril 2023
# Datos de salida (Q reclamos terreno)
y = np.array([70, 77, 84, 252, 254, 126, 89, 89, 97, 97, 102, 146, 132, 115, 141, 171, 161, 147, 145, 171, 169, 172])  # Calidad terreno

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X, y)

# Predecir cantidad de goles mundial 2026(mundial 23)
mayo = np.array([[23]])
prediccion = int(model.predict(mayo))

print("La prediccion de goles para el mundial Canadá, Estados Unidos y México 2026 es:", prediccion)

# Plotear los datos y la línea de regresión
plt.scatter(X, y, color='b', label='Datos')
plt.plot(X, model.predict(X), color='r', label='Línea de regresión')
plt.scatter(mayo, prediccion, color='g', label='Predicción')
plt.xlabel('Meses')
plt.ylabel('Cantidad de goles por mundial de futbol')
plt.title('Regresión lineal')
plt.legend()
plt.show()
