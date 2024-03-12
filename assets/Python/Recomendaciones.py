# Datos de usuarios y productos
usuarios = {
    1: {'Edad': 25, 'Sexo': 'M', 'Ubicación': 'Santiago'},
    2: {'Edad': 30, 'Sexo': 'F', 'Ubicación': 'Valparaíso'},
    3: {'Edad': 40, 'Sexo': 'M', 'Ubicación': 'Viña del Mar'},
    4: {'Edad': 18, 'Sexo': 'F', 'Ubicación': 'Concepción'}
}

productos = {
    1: {'Categoría': 'Película', 'Precio': 5.00, 'Descripción': 'El Señor de los Anillos: La Comunidad del Anillo'},
    2: {'Categoría': 'Libro', 'Precio': 10.00, 'Descripción': 'Cien años de soledad'},
    3: {'Categoría': 'Zapatilla', 'Precio': 20.00, 'Descripción': 'Nike Air Force 1'},
    4: {'Categoría': 'Smartphone', 'Precio': 500.00, 'Descripción': 'Samsung Galaxy S23'}
}

# Calcular la similitud entre usuarios
def similitud_usuario(usuario1, usuario2):
    similitud = 0
    for clave in usuario1:
        if clave in usuario2:
            if usuario1[clave] == usuario2[clave]:
                similitud += 1
    return similitud

# Recomendar productos para un usuario dado
def recomendar_producto(usuario_id):
    similaridad_max = -1
    usuario_similar = None
    for id, usuario in usuarios.items():
        if id != usuario_id:
            similitud = similitud_usuario(usuarios[usuario_id], usuario)
            if similitud > similaridad_max:
                similaridad_max = similitud
                usuario_similar = id
    
    productos_recomendados = []
    for producto_id, producto in productos.items():
        if producto_id not in productos_recomendados:
            productos_recomendados.append(producto_id)
    return productos_recomendados

# Ejemplo de recomendación para un usuario específico
usuario_id = 1
print("Recomendaciones para el Usuario", usuario_id)
print(recomendar_producto(usuario_id))