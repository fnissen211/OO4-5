from socket import *
import threading
import random

def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()

        if sentence.strip().lower() == 'close':
            connectionSocket.send("connection closed".encode())
            connectionSocket.close()
            break
        elif sentence.strip().lower() == 'random':
            connectionSocket.send("input message:\n".encode())
            numbers = connectionSocket.recv(1024).decode()
            try: 
                num1, num2 = map(int, numbers.split())
                result = random.randrange(num1, num2)
                connectionSocket.send((str(result) + "\n").encode())
            except ValueError:
                connectionSocket.send("The first number MUST be the smallest number.\n".encode())
        elif sentence.strip().lower() == 'add':
            connectionSocket.send("input message:\n".encode())
            numbers = connectionSocket.recv(1024).decode()
            try: 
                num1, num2 = map(int, numbers.split())
                result = num1 + num2
                connectionSocket.send((str(result) + "\n").encode())
            except ValueError:
                connectionSocket.send("Please input two valid numbers separated by a space\n".encode())
        elif sentence.strip().lower() == 'subtract':
            connectionSocket.send("input message:\n".encode())
            numbers = connectionSocket.recv(1024).decode()
            try: 
                num1, num2 = map(int, numbers.split())
                result = num1 - num2
                connectionSocket.send((str(result) + "\n").encode())
            except ValueError:
                connectionSocket.send("Please input two valid numbers separated by a space\n".encode())

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket, addr)).start()
