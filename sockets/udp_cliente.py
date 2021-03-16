from socket import *

server_host = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.connect((server_host, server_port))

frase = input("Digite uma frase: ")

client_socket.send(frase.encode())

frase_data_hora = client_socket.recv(2048)
print("Frase recebida: ", frase_data_hora.decode())

client_socket.close()
