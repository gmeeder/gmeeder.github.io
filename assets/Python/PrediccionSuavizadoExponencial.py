import numpy as np
import matplotlib.pyplot as plt

# Serie temporal de ejemplo
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Coeficiente de suavizado
alpha = 0.2

# Inicialización de la predicción
predictions = [data[0]]

# Cálculo de la predicción para cada punto de datos
for i in range(1, len(data)):
    pred = alpha * data[i - 1] + (1 - alpha) * predictions[-1]
    predictions.append(pred)

# Predicción del siguiente valor
next_prediction = alpha * data[-1] + (1 - alpha) * predictions[-1]

# Graficar la serie temporal y las predicciones
plt.plot(data, label='Serie Temporal', marker='o')
plt.plot(range(1, len(data) + 1), predictions, label='Predicciones', marker='x')
plt.scatter(len(data) + 1, next_prediction, color='red', label='Predicción siguiente valor', marker='*')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Predicción de siguiente valor en la serie temporal')
plt.legend()
plt.show()

print("Predicción del siguiente valor:", next_prediction)
