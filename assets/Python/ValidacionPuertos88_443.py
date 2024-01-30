import requests
import socket

host = 'www.nambla.org'

# Verificar si los puertos 80 y 443 están abiertos
for port in [80, 443]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

# Hacer una solicitud HTTP al puerto 80
try:
    response = requests.get(f'http://{host}/index.html', timeout=5)
    print(f"HTTP status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"HTTP request failed: {e}")

# Hacer una solicitud HTTPS al puerto 443
try:
    response = requests.get(f'https://{host}/index.html', timeout=5)
    print(f"HTTPS status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"HTTPS request failed: {e}")