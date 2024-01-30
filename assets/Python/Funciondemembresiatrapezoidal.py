import numpy as np
import matplotlib.pyplot as plt

# Definir una función de membresía trapezoidal
def trapezoidal(x, a, b, c, d):
    if x <= a or x >= d:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif c < x < d:
        return (d - x) / (d - c)
    else:
        return 1.0

# Definir los parámetros de la función de membresía trapezoidal
a = 2
b = 4
c = 6
d = 8

# Crear un array de valores de entrada para evaluar la función de membresía
x = np.linspace(0, 10, 1000)

# Evaluar la función de membresía trapezoidal en los valores de entrada
y = np.array([trapezoidal(i, a, b, c, d) for i in x])

# Graficar la función de membresía trapezoidal
plt.plot(x, y)
plt.xlabel('Valor de entrada')
plt.ylabel('Grado de pertenencia')
plt.title('Función de membresía trapezoidal')
plt.show()