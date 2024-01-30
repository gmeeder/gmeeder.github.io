import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Crear universo (rango de valores posibles)
x = np.arange(0, 11, 0.1)

# Crear conjunto difuso discreto
bajo = fuzz.trimf(x, [0, 0, 5])
medio = fuzz.trimf(x, [0, 5, 10])
alto = fuzz.trimf(x, [5, 10, 10])

# Crear conjunto difuso continuo
saturacion = fuzz.trapmf(x, [0, 2, 8, 10])
brillo = fuzz.gaussmf(x, 5, 1.5)

# Graficar los conjuntos
fig, ax = plt.subplots()

ax.plot(x, bajo, 'b', linewidth=1.5, label='Bajo')
ax.plot(x, medio, 'g', linewidth=1.5, label='Medio')
ax.plot(x, alto, 'r', linewidth=1.5, label='Alto')

ax.plot(x, saturacion, 'c', linewidth=1.5, label='Saturacion')
ax.plot(x, brillo, 'm', linewidth=1.5, label='Brillo')

ax.set_title('Conjuntos Difusos Discretos y Continuos')
ax.legend()

plt.show()