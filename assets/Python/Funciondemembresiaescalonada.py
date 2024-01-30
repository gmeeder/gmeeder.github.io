def membership_func(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a <= x <= b:
        return (x-a)/(b-a)
    elif c <= x <= d:
        return (d-x)/(d-c)
    else:
        return 1

# Ejemplo de uso
x = range(-10, 11)
y = [membership_func(i, -5, 0, 5, 10) for i in x]

# Graficar función de membresía escalonada
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función de membresía escalonada')
plt.grid(True)
plt.show()