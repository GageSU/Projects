from socket import *
import random
import json

serverPort = 7501

#Create socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

#Command to reuse same socket over and over again
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

#Start listening
serverSocket.bind(('', serverPort))
print('Server is ready to recieve')

#Continue listening forever
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode('utf-8')
    #Constantly read files due to changing teams from game to game
    IDs = []
    with open('redID.txt', 'r') as file:
        p = json.load(file)
        for i in p:
            IDs.append(i)
    with open('greenID.txt', 'r') as file:
        p = json.load(file)
        for i in p:
            IDs.append(i)

    playerID = random.choice(IDs)
    while int(decodedMessage) == int(playerID):
        playerID = random.choice(IDs)
    newMessage = str(decodedMessage) + ':' + str(playerID)
    print(newMessage)
    newMessageBytes = newMessage.encode('utf-8')
    serverSocket.sendto(newMessageBytes, clientAddress)
