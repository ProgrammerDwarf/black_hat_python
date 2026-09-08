import socket

host = '127.0.0.1'
port = 9997

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))

print(f"Servidor UDP escuchando en {host}:{port}...")

while True:
    data, addr = server.recvfrom(4096)
    print(f"Mensaje recibido de {addr}: {data.decode()}")
    server.sendto(b"Servidor responde: Mensaje recibido correctamente!", addr)