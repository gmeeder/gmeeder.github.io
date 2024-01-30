import socket


ip_address = '162.241.61.64'
ports = [3128, 8080, 80, 443, 8443, 1080] # Lista de puertos comunes para proxies

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5) # Establece un tiempo de espera para la conexión
    result = sock.connect_ex((ip_address, port))
    
    if result == 0:
        print("El puerto", port, "está abierto y puede ser un proxy")
    sock.close()