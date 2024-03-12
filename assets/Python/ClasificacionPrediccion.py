# Definir palabras clave asociadas con spam
palabras_spam = ["oferta", "gana dinero", "adelgaza", "viagra", "infectado", "haz clic aquí"]

# Función para determinar si un correo electrónico es spam o no
def es_spam(asunto, mensaje):
    # Convertir el asunto y el mensaje a minúsculas para una comparación sin distinción entre mayúsculas y minúsculas
    asunto = asunto.lower()
    mensaje = mensaje.lower()
    
    # Verificar si alguna palabra clave de spam está presente en el asunto o el mensaje
    for palabra in palabras_spam:
        if palabra in asunto or palabra in mensaje:
            return True
    
    return False

# Ejemplo de uso
asunto = "Oferta especial de adelgazamiento"
mensaje = "¡Pierde peso rápidamente con nuestro nuevo producto!"
if es_spam(asunto, mensaje):
    print("Este correo electrónico parece ser spam.")
else:
    print("Este correo electrónico parece ser legítimo.")