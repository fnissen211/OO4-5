from socket import *
import random

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

def ServerRespons(sentence):
    if clientSentence.strip().lower() == "add":
        if sentence.strip().lower() == "input numbers":
            sentence = input('Input two numbers: \n')
            try:
                num1, num2 = map(int, sentence.split())
                clientSocket.send((str(num1 + num2) + "\n").encode())
            except ValueError:
                clientSocket.send("Input two numbers with space inbetween. \n".encode())
        else:
            sentence = input('Wrong format. Please input one of the functions Add, Subtract or Random: \n')
            clientSocket.send(sentence.encode())
    elif clientSentence.strip().lower() == "subtract":
        if sentence.strip().lower() == "input numbers":
            sentence = input('Input two numbers: ')
            try:
                num1, num2 = map(int, sentence.split())
                clientSocket.send((str(num1 - num2) + "\n").encode())
            except ValueError:
                clientSocket.send("Input two numbers with space inbetween. \n".encode())
        else:
            sentence = input('Wrong format. Please input one of the functions Add, Subtract or Random: \n')
            clientSocket.send(sentence.encode())
    elif clientSentence.strip().lower() == "random":
        if sentence.strip().lower() == "input numbers":
            sentence = input('Input two numbers: ')
            try: 
                num1, num2 = map(int, sentence.split())
                result = random.randrange(num1, num2)
                clientSocket.send((str(result) + "\n").encode())
            except ValueError:
                clientSocket.send("The first number MUST be the smallest number.\n".encode())
        else:
            sentence = input('Wrong format. Please input one of the functions Add, Subtract or Random: \n')
            clientSocket.send(sentence.encode())

while True:
    clientSentence = input('Input function Add, Subtract or Random: \n')
    clientSocket.send(clientSentence.encode())
    serverSentence = clientSocket.recv(1024)
    ServerRespons(serverSentence.decode())

