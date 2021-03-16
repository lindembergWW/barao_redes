from socket import *
from datetime import datetime

# Numero da porta
server_host = 'localhost'
server_port = 12000

# Inicia socket de conexao
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('',server_port))

print("Servidor online e ouvindo")

def add_data_hora(msg):
    frase = msg.decode()
    data_hora = str(datetime.now())
    return frase + " : " + data_hora

while True:
    msg, client_address = server_socket.recvfrom(2048)
    print("Conectando com ", client_address)
    frase_data_hora = add_data_hora(msg)
    server_socket.sendto(frase_data_hora.encode(), client_address)

