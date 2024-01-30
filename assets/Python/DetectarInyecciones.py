import re
import urllib.request

# Lista de patrones para validar las posibles inyecciones
patterns = {
    "Inyección SQL": [r"['\";=]"],
    "Inyección Cross-site scripting (XSS)": [r"<script>|</script>|<html>|</html>"],
    "Inyección Cross-site request forgery (CSRF)": [r"csrf_token="],
    "Inyección de código PHP": [r"<\?php|\?>"],
    "Inyección de código JavaScript": [r"<script>|</script>"],
    "Inyección LDAP": [r"[\\(\\)&|!]"],
    "Inyección de comandos": [r"[;&|]"],
    "Inyección XPath": [r"['\"]|//"],
    "Inyección de código en plantillas": [r"{{|}}"],
    "Inyección de XML": [r"['\"]|<|>"],
    "Inyección de SSI": [r"<!--#|-->|<!--"],
    "Inyección de código en cookies": [r"document.cookie|cookie=|setcookie"],
    "Inyección de cabeceras HTTP": [r"[<>\"']"],
    "Inyección de metadatos": [r"<meta>|</meta>|<link>|</link>"],
    "Inyección de archivos": [r"\.\./|\.\.\\|~"],
    "Inyección de objetos serializados": [r"O:[0-9]+:\""],
    "Inyección de código en atributos": [r"on[a-z]*=|javascript:"],
    "Inyección de archivos JSON": [r"\.json"],
    "Inyección de archivos CSV": [r"\.csv"],
    "Inyección de archivos XML externos": [r"<!ENTITY"]
}

# Función que valida todas las posibles inyecciones en un string
def validate_input(input_string):
    vulnerabilities = []
    for category, patterns_list in patterns.items():
        for pattern in patterns_list:
            if re.search(pattern, input_string):
                vulnerabilities.append(category)
                break
    if vulnerabilities:
        print("El string contiene posibles inyecciones en las siguientes categorías:", vulnerabilities)
    else:
        print("El string no contiene posibles inyecciones")

# Ejemplo de uso
input_string = "SELECT * FROM users WHERE username = 'admin';"
validate_input(input_string)

# Ejemplo con URL
url = "https://partidodelagente.cl/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read().decode()

validate_input(html)