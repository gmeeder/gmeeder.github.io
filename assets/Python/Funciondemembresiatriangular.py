import numpy as np
import matplotlib.pyplot as plt

def triangular(x, a, b, c):
    # Definir la función triangular
    if x <= a or x >= c:
        return 0
    elif x >= a and x <= b:
        return (x - a) / (b - a)
    elif x >= b and x <= c:
        return (c - x) / (c - b)

# Definir los parámetros de la función triangular
a = 0
b = 5
c = 10

# Evaluar la función triangular en un rango de valores
x = np.arange(-1, 11, 0.1)
y = [triangular(i, a, b, c) for i in x]

# Graficar la función triangular
plt.plot(x, y)
plt.title('Función de membresía triangular')
plt.xlabel('x')
plt.ylabel('y')
plt.show()