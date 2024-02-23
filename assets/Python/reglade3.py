import tkinter as tk
from tkinter import font

def calcular_regla_de_tres():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        num3 = float(entrada3.get())

        resultado = (num3 * num2) / num1

        resultado_label.config(text=f"El resultado es: {resultado}", font=("Arial", 14))
    except ValueError:
        resultado_label.config(text="Por favor, introduce números válidos", font=("Arial", 14))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Regla de Tres")

# Crear los widgets
label1 = tk.Label(ventana, text="Número 1:", font=("Arial", 16))
label2 = tk.Label(ventana, text="Número 2:", font=("Arial", 16))
label3 = tk.Label(ventana, text="Número 3:", font=("Arial", 16))

entrada1 = tk.Entry(ventana, font=("Arial", 16))
entrada2 = tk.Entry(ventana, font=("Arial", 16))
entrada3 = tk.Entry(ventana, font=("Arial", 16))

calcular_button = tk.Button(ventana, text="Calcular", font=("Arial", 16), command=calcular_regla_de_tres)
resultado_label = tk.Label(ventana, font=("Arial", 16))

# Colocar los widgets en la ventana
label1.grid(row=0, column=0, padx=10, pady=10)
entrada1.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entrada2.grid(row=1, column=1, padx=10, pady=10)
label3.grid(row=2, column=0, padx=10, pady=10)
entrada3.grid(row=2, column=1, padx=10, pady=10)

calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Configurar el tamaño de la ventana
ventana.geometry("400x300")

# Iniciar el bucle de eventos
ventana.mainloop()
