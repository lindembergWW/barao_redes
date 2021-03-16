from socket import *

# Numero da porta
server_port = 12000

# Inicia socket de conexao
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('',server_port))
server_socket.listen(1)

print("Servidor online e ouvindo")

def inverter_mensagem(msg):
    frase = msg.decode()
    print("Invertendo frase: ", frase)
    frase_invertida = "".join(reversed(frase))
    return frase_invertida

while True:
    connection_socket, client_address = server_socket.accept()
    print("Conectando com ", client_address)
    msg = connection_socket.recv(2048)
    frase_invertida = inverter_mensagem(msg)
    connection_socket.send(frase_invertida.encode())
    connection_socket.close()


