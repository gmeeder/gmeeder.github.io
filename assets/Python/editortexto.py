import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            entrada_texto.delete('1.0', tk.END)
            entrada_texto.insert(tk.END, contenido)

def guardar_archivo():
    ruta_archivo = filedialog.asksaveasfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta_archivo:
        with open(ruta_archivo, 'w') as archivo:
            contenido = entrada_texto.get('1.0', tk.END)
            archivo.write(contenido)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")

# Botón para abrir archivo
boton_abrir = tk.Button(ventana, text="Abrir archivo", command=abrir_archivo)
boton_abrir.pack()

# Entrada de texto para editar el contenido
entrada_texto = tk.Text(ventana, wrap="word")
entrada_texto.pack()

# Botón para guardar archivo
boton_guardar = tk.Button(ventana, text="Guardar archivo", command=guardar_archivo)
boton_guardar.pack()

# Ejecutar la aplicación
ventana.mainloop()
