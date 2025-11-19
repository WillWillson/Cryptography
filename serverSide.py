from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',12000))
serverSocket.listen(1)
print("Server is ready to connect... \n")


while(True):
    connectionSocket, address = serverSocket.accept()
    print("connection Established with: {}".format(address))

    incomingMessage = connectionSocket.recv(2048)
    print("Receive message: {}".format(incomingMessage.decode()))

    mdoifiedMessage = incomingMessage.upper()
    print("modified message: {}".format(modifiedMessage.decode()))

    connectionSocket.send(modifiedMessage)
    print("Message sent...\n")

    connectionSocket.close()
