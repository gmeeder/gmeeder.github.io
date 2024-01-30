def membership_func(t):
    if t % 2 == 0:
        return 1
    else:
        return 0.5

# Ejemplo de uso
X = range(1, 11)
Y = [membership_func(t) for t in X]

# Graficar función de membresía para conjunto difuso "números pares"
import matplotlib.pyplot as plt

plt.plot(X, Y)
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Función de membresía para conjunto difuso "números pares"')
plt.grid(True)
plt.show()