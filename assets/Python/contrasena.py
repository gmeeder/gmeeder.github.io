import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import string
import random

def generate_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número entero para la longitud de la contraseña.")
        return

    if length <= 0:
        messagebox.showerror("Error", "La longitud de la contraseña debe ser mayor que cero.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    text_password.delete(1.0, tk.END)
    text_password.insert(tk.END, password)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Contraseña")

# Marco principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiqueta y entrada para la longitud de la contraseña
label_length = ttk.Label(frame, text="Longitud de la contraseña:")
label_length.grid(row=0, column=0, sticky=tk.W)

entry_length = ttk.Entry(frame)
entry_length.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Botón para generar contraseña
button_generate = ttk.Button(frame, text="Generar Contraseña", command=generate_password)
button_generate.grid(row=1, columnspan=2, pady=5)

# Campo de texto para mostrar la contraseña generada
text_password = tk.Text(frame, width=50, height=5)
text_password.grid(row=2, columnspan=2, padx=5, pady=5)

# Barra de desplazamiento para el campo de texto
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=text_password.yview)
scrollbar.grid(row=2, column=2, sticky=(tk.N, tk.S))
text_password.config(yscrollcommand=scrollbar.set)

# Ejecutar el bucle de eventos
root.mainloop()
