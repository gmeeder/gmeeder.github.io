import numpy as np
import matplotlib.pyplot as plt

def gaussiana(x, media, desviacion):
    # Definir la función gaussiana
    return np.exp(-(x - media)**2 / (2 * desviacion**2))

# Definir los parámetros de la función gaussiana
media = 5
desviacion = 2

# Evaluar la función gaussiana en un rango de valores
x = np.arange(0, 10, 0.1)
y = gaussiana(x, media, desviacion)

# Graficar la función gaussiana
plt.plot(x, y)
plt.title('Función de membresía gaussiana')
plt.xlabel('x')
plt.ylabel('y')
plt.show()