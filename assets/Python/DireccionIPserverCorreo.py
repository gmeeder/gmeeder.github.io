import dns.resolver

def get_mail_server_ip(domain):
    try:
        # Obtener los registros MX del dominio
        mx_records = dns.resolver.resolve(domain, 'MX')

        # Tomar el primer registro MX
        mail_server = str(mx_records[0].exchange)

        # Obtener la dirección IP del servidor de correo
        mail_server_ip = dns.resolver.resolve(mail_server, 'A')[0].to_text()

        return mail_server_ip

    except dns.resolver.NoAnswer:
        print(f"No se pudo encontrar el servidor de correo para el dominio {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"No se pudo encontrar el dominio {domain}")
    except dns.resolver.Timeout:
        print(f"Tiempo agotado al resolver el dominio {domain}")

# Ejemplo de uso
domain = 'google.com'
mail_server_ip = get_mail_server_ip(domain)
print(f"La dirección IP del servidor de correo de {domain} es: {mail_server_ip}")