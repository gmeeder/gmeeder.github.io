import numpy as np
import matplotlib.pyplot as plt

datos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
siguiente_valor = datos[-1] + 1

pendiente = np.sum((datos[:-1] - np.mean(datos[:-1])) * (datos[1:] - np.mean(datos[1:]))) / np.sum((datos[:-1] - np.mean(datos[:-1]))**2)
intercepto = np.mean(datos) - pendiente * np.mean(datos[:-1])

prediccion = pendiente * siguiente_valor + intercepto

# Graficar la regresión lineal
plt.plot(datos[:-1], datos[1:], 'o', color='blue')
x = np.linspace(datos.min(), datos.max(), 100)
y = pendiente * x + intercepto
plt.plot(x, y, color='red')


plt.title('Regresión lineal para predecir el siguiente valor')
plt.legend(['Puntos del histórico', 'Línea de regresión'], loc='best')
plt.plot(siguiente_valor, prediccion, '^', color='green')
plt.annotate('Valor predicho', (siguiente_valor, prediccion), xytext=(0, 5), textcoords='offset points', arrowprops=dict(arrowstyle='->'))
plt.xlabel('Valor anterior')
plt.ylabel('Siguiente valor')
plt.show()

print(f"Predicción del siguiente valor: {prediccion}")
