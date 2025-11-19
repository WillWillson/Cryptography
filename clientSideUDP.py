from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Socket has been created...\n")

serverIp = input("Server IP: ")
serverPort = input("Server Port: ")
message = input("Message: ")

clientSocket.sendto(message.encode(), (serverIp, int(serverPort)))
print("\nSent message: {}\nTo Server: {}".format(message, (serverIp, int(serverPort))))

recvMessage, serverAddress = clientSocket.recvfrom(2048)
print("Received message: {}\nFrom Server: {}".format(recvMessage.decode(), serverAddress))

clientSocket.close()
