from socket import *

server_host = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))

frase = input("Digite uma frase: ")

client_socket.send(frase.encode())

frase_invertida = client_socket.recv(1024)
print("Frase invertida recebida: ", frase_invertida.decode())

client_socket.close()
