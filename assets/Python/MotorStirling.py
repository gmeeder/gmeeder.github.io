import numpy as np
import matplotlib.pyplot as plt

# Solicitar datos del Motor Stirling
V_max = float(input("Ingrese el volumen máximo [cm^3]: "))
V_min = float(input("Ingrese el volumen mínimo [cm^3]: "))
P_max = float(input("Ingrese la presión máxima [bar]: "))
P_min = float(input("Ingrese la presión mínima [bar]: "))
n_points = int(input("Ingrese el número de puntos en el ciclo: "))

# Calcula el volumen y la presión en cada punto del ciclo
V = np.linspace(V_min, V_max, n_points)
P = np.zeros(n_points)
T = np.zeros(n_points)

for i in range(n_points):
    P[i] = P_min + (P_max - P_min) * (V_max / V[i])
    T[i] = P[i] * V[i] / (8.31 * 273)  # Ley del gas ideal (R=8.31 J/(mol*K))

# Calcula la gradiente dP/dV
dP_dV = np.gradient(P, V)

# Crea el diagrama PV
plt.figure(figsize=(8, 6))
plt.plot(V, P)
plt.xlabel('Volumen (cm^3)')
plt.ylabel('Presión (bar)')
plt.title('Diagrama PV del Ciclo Stirling')
plt.grid()
plt.show()

# Crea el diagrama dP/dV
plt.figure(figsize=(8, 6))
plt.plot(V, dP_dV)
plt.xlabel('Volumen (cm^3)')
plt.ylabel('Gradiente dP/dV (bar/cm^3)')
plt.title('Gradiente de Presión con respecto al Volumen')
plt.grid()
plt.show()