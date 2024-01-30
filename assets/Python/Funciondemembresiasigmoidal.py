import numpy as np

def sigmoid(x, c, a):
    y = 1 / (1 + np.exp(-a*(x-c)))
    return y

# Ejemplo de uso
x = np.linspace(-10, 10, num=100)
y = sigmoid(x, 0, 1)

# Graficar función de membresía sigmoidal
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función de membresía sigmoidal')
plt.grid(True)
plt.show()