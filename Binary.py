import sys

file = open(sys.argv[1], "r")
binaryMessage = file.read()

if (((len(binaryMessage)-1)/7) % 1 == 0):
    bitSize = 7
elif (((len(binaryMessage)-1)/8) % 1 == 0):
    bitSize = 8
    
print(''.join(chr(int(binaryMessage[i*bitSize:i*bitSize+bitSize],2)) for i in range(len(binaryMessage)//bitSize)))
    
