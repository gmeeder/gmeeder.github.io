import socket

def check_dbms(host, port):
    # Intenta conectar con el host y puerto dados
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)  # tiempo límite de espera de conexión
        s.connect((host, port))
        s.send(b'\x00')  # envía un mensaje vacío para probar la conexión
        response = s.recv(1024)
        s.close()
        
        # Comprueba la respuesta recibida para determinar el DBMS
        if b'mysql_native_password' in response:
            return 'MySQL'
        elif b'PostgreSQL' in response:
            return 'PostgreSQL'
        elif b'Oracle' in response:
            return 'Oracle'
        elif b'Microsoft SQL Server' in response:
            return 'Microsoft SQL Server'
        else:
            return 'Desconocido'
    except:
        return 'No disponible'

# Ejemplo de uso
host = '45.236.165.90'  # dirección IP o nombre del servidor
mysql_port = 3306
postgres_port = 5432
oracle_port = 1521
sqlserver_port = 1433

dbms_mysql = check_dbms(host, mysql_port)
dbms_postgres = check_dbms(host, postgres_port)
dbms_oracle = check_dbms(host, oracle_port)
dbms_sqlserver = check_dbms(host, sqlserver_port)

print(f"DBMS en {host}:")
print(f"MySQL: {dbms_mysql}")
print(f"PostgreSQL: {dbms_postgres}")
print(f"Oracle: {dbms_oracle}")
print(f"Microsoft SQL Server: {dbms_sqlserver}")