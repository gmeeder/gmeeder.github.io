import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Conjuntos difusos discretos

# Se definen los elementos del conjunto difuso
x_pts = [1, 2, 3, 4, 5]
y_pts = [0, 0.2, 0.6, 0.8, 1]

# Se interpola cada elemento para construir una trayectoria
x_interp = np.linspace(min(x_pts), max(x_pts), num=101, endpoint=True)
y_interp = np.interp(x_interp, x_pts, y_pts)

# Se grafica la trayectoria
plt.figure(figsize=(8, 4))
plt.plot(x_interp, y_interp, 'b', linewidth=1.5, label='Trayectoria')
plt.ylabel('Grado de pertenencia')
plt.xlabel('Valor')
plt.title('Conjunto difuso discreto')
plt.legend(loc='center')
plt.show()

# Conjuntos difusos continuos

# Se crea el universo (rango de valores posibles)
x = np.linspace(0, 10, 101)

# Se definen las funciones de pertenencia
bajo = fuzz.trimf(x, [0, 0, 5])
medio = fuzz.trimf(x, [0, 5, 10])
alto = fuzz.trimf(x, [5, 10, 10])

# Se grafican las funciones de pertenencia
plt.figure(figsize=(8, 4))
plt.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(x, medio, 'g', linewidth=1.5, label='Medio')
plt.plot(x, alto, 'r', linewidth=1.5, label='Alto')
plt.ylabel('Grado de pertenencia')
plt.xlabel('Valor')
plt.title('Conjunto difuso continuo')
plt.legend(loc='center')
plt.show()