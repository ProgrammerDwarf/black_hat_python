import socket
import ssl  # 1. Importar el módulo SSL

target_host = 'www.google.com'
target_port = 443  # 2. Cambiar al puerto seguro HTTPS

# Creación de objeto socket base
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Crear el envoltorio SSL para cifrar la conexión
context = ssl.create_default_context()
client = context.wrap_socket(raw_socket, server_hostname=target_host)

# Conexión con el servidor
client.connect((target_host, target_port))

# Enviar datos (Asegúrate de pedir 'www.google.com')
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n")

# Recibir datos
response = client.recv(4096)

print(response.decode('utf-8', errors='ignore'))
client.close()