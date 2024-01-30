import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

host = '45.236.165.90'  # Cambia esto por el nombre de tu host
for port in range(1, 1025):
    if check_port(host, port):
        print(f"El puerto {port} está abierto")