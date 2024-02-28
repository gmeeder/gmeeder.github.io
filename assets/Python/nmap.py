import subprocess

art = """
                                                                                                                                                                                                                                              
                                        _----..................___
     __,,..,             _,.--''------'' |   _____  ______________`''--._
     \      `\   __..--''                |  /::: / /::::::::::::::\      `\\
      \       `''                        | /____/ /___ ____ _____::|    .  \\
       \      ++ Navaja NMAP ++    ,.... |            `    `     \_|   ( )  |
        `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
          `.                     |        ,'       `               `-.      |
            `-._                 \                                    ``.. /
                `---..............> ++ Detectecta vulneravilidades ++
                                    ++ usando los script disponibles ++

++<< /dev/null antes que el deshonor >>++
!!!Se requiere tener instalado NMAP en el dipositivo¡¡¡

 «trata a los demás como querrías que te trataran a ti»
 o 
 «no hagas a los demás lo que no quieras que te hagan a ti»

"""

print(art)


# Función para solicitar una URL
def solicitar_url():
    url = input("Ingresa una URL: ")
    return url

# Función para mostrar el menú y obtener la opción seleccionada
def mostrar_menu():
    print("++- MENU -++")
    print("1. http-title")
    print("2. ssl-enum-ciphers")
    print("3. ftp-anon")
    print("4. smtp-enum-users")
    print("5. smb-vuln-*")
    print("6. dns-zone-transfer")
    print("7. snmp-*")
    print("8. ssh-brute")
    print("9. mysql-*")
    print("10. vnc-*")
    print("11. vuln")
    print("0. Salir del programa")
    print("")
    opcion = int(input("Herman@, que Script deseas usar: "))
    return opcion

# Función para ejecutar el comando en la URL y mostrar los resultados
def ejecutar_comando(url, opcion):
    comando = "nmap -A --script"

    if opcion == 1:
        comando += " http-title"
    elif opcion == 2:
        comando += " ssl-enum-ciphers"
    elif opcion == 3:
        comando += " ftp-anon"
    elif opcion == 4:
        comando += " smtp-enum-users"
    elif opcion == 5:
        comando += " smb-vuln-*"
    elif opcion == 6:
        comando += " dns-zone-transfer"
    elif opcion == 7:
        comando += " snmp-*"
    elif opcion == 8:
        comando += " ssh-brute"
    elif opcion == 9:
        comando += " mysql-*"
    elif opcion == 10:
        comando += " vnc-*"
    elif opcion == 11:
        comando += " vuln"
    elif opcion == 0:
        return False

    comando += " " + url

    print("Se esta ejecutando el siguiente comando:", comando)

    # Ejecutar el comando y capturar la salida
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    # Mostrar la salida del comando
    print("\n--++--++------ El resultado al mapedo solicitado es: ------++--++--")
    print(resultado.stdout)

    return True

# Solicitar la URL
url = solicitar_url()

while True:
    # Mostrar el menú y obtener la opción seleccionada
    opcion = mostrar_menu()

    # Verificar la opción seleccionada
    if opcion == 0:
        break
    else:
        # Ejecutar el comando en la URL y mostrar los resultados
        continuar = ejecutar_comando(url, opcion)
        if not continuar:
            break

