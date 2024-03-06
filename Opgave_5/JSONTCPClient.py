from socket import *
import json

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

try:
    while True:
        func = input('Input function Add, Subtract or Random and two numbers: ')
        num1 = input('Input the first number: ')
        num2 = input('Input function Add, Subtract or Random and two numbers: ')

        clientRequest = {"function": func, "num1": num1, "num2": num2}
        clientSocket.send(json.dumps(clientRequest).encode())
        input('Request has been send.\n')
        serverSentence = clientSocket.recv(1024).decode()
        try:
            serverSentenceJSON = json.loads(serverSentence)
            print("Response:", serverSentenceJSON)
        except json.JSONDecodeError as e:
            print("Error decoding JSON response:", e)
except KeyboardInterrupt:
    print("Exiting client...")
finally:
    clientSocket.close()