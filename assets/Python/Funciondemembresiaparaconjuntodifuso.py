def membership_func(t):
    if t >= 0 and t <= 10:
        return 1 - (t/10)
    elif t > 10 and t <= 20:
        return (t-10)/10
    else:
        return 0

# Ejemplo de uso
X = range(-5, 26)
Y = [membership_func(t) for t in X]

# Graficar función de membresía para conjunto difuso
import matplotlib.pyplot as plt

plt.plot(X, Y)
plt.xlabel('t')
plt.ylabel('u(t)')
plt.title('Función de membresía para conjunto difuso')
plt.grid(True)
plt.show()