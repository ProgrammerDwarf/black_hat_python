import socket

#target_host = 'www.google.com'
target_host = '127.0.0.1'
#target_port = 80
target_port = 9998

# Creación de objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexión con un cliente
client.connect((target_host, target_port))

# Enviar datos
client.send(b"GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")

# Recibir datos
response = client.recv(4096)

print(response.decode())
client.close()