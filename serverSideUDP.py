from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Server is ready to receive messages...\n")

while(True):
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Message: {}".format(message.decode(), clientAddress))

    modifiedMessage = message.upper()
    print("Modified message: {}".format(modifiedMessage.decode()))

    serverSocket.sendto(modifiedMessage, clientAddress)
    print("Message sent\n")
