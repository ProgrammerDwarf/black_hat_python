import socket

target_host = 'www.google.com'
target_port = 80

# Creación de objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexión con un cliente
client.connect((target_host, target_port))

# Enviar datos
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Recibir datos
response = client.recv(4096)

print(response.decode())
client.close()