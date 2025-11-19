from socket import *

clientSocket= socket(AF_INET, SOCK_STREAM)

serverIp = input("Server IP:")
serverPort = input("Server port: ")

clientSocket.connect((serverIp, int(serverPort)))

print("Connection is established...\n")

message = input("Message: ")

clientSocket.send(message.encode())
print("Message sent...")

receivedMessage = clientSocket.recv(2048)
print("Received message: {}".format(receivedMessage.decode()))

clientSocket.close()
