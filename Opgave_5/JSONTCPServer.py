from socket import *
import threading
import json
import random

def handleClient(connectionSocket, address):
    connectionSocket.send('Enter the data in the following format and replace the xx, with data: \n{"function":"add/subtract/random", "num1":xx, "num2":xx}\n'.encode())  
    try:
        while True:
            try:
                clientSentence = connectionSocket.recv(1024).decode()
                if not clientSentence:
                    print("Client {} disconnected.".format(address))
                    break
                convertToPY = json.loads(clientSentence)

                func = convertToPY.get("function")
                num1 = convertToPY.get("num1")
                num2 = convertToPY.get("num2")

                if func == "add":
                    result = num1 + num2
                    noErrors = True
                elif func == "subtract":
                    result = num1 - num2
                    noErrors = True
                elif func == "random":
                    try:
                        result = random.randrange(num1, num2)
                        noErrors = True
                    except ValueError:
                        connectionSocket.send("num1 MUST be the smallest number.\n".encode())
                        noErrors = False
                if noErrors:
                    convertResult = {"result": result}
                    connectionSocket.send((json.dumps(convertResult) + "\n").encode())
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
    except ConnectionResetError:
        print("Connection with client {} was reset.".format(address))

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket, addr)).start()