import tkinter as tk
from tkinter import ttk
import json

def cargar_productos():
    try:
        with open('productos.json', 'r', encoding='utf-8') as file:  # Especificamos la codificación como 'utf-8'
            data = json.load(file)
            return data['productos']
    except FileNotFoundError:
        print("El archivo productos.json no se encontró.")

class ProductosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Productos")

        self.productos = cargar_productos()

        self.tree = ttk.Treeview(self.root)
        self.tree['columns'] = ('ID', 'NOMBRE', 'DESCRIPCIÓN', 'PRECIO')

        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=50)
        self.tree.column('NOMBRE', anchor=tk.CENTER, width=150)
        self.tree.column('DESCRIPCIÓN', anchor=tk.CENTER, width=300)
        self.tree.column('PRECIO', anchor=tk.CENTER, width=100)

        self.tree.heading('#0', text='', anchor=tk.CENTER)
        self.tree.heading('ID', text='ID', anchor=tk.CENTER)
        self.tree.heading('NOMBRE', text='Nombre', anchor=tk.CENTER)
        self.tree.heading('DESCRIPCIÓN', text='Descripción', anchor=tk.CENTER)
        self.tree.heading('PRECIO', text='Precio', anchor=tk.CENTER)

        for producto in self.productos:
            self.tree.insert('', 'end', text='', values=(producto['ID'], producto['NOMBRE'], producto['DESCRIPCION'], producto['PRECIO']))

        self.tree.pack(expand=True, fill=tk.BOTH)

def main():
    root = tk.Tk()
    app = ProductosApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
