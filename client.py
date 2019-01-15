
import time
from socket import *
import threading
import sys

serverName="192.168.0.26"
serverPort=12000

clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
class Client():

    def receive(self):

        while True:
            message2 = clientSocket.recv(1024)
            if message2 == "exit":
                exit(0)
            print ": ", message2.decode("utf-8"), time.strftime("%H:%M:%S")

    def __init__(self):

        while True:
            threading.Thread(target=self.receive, ).start()
            message = input()
            clientSocket.send(message.encode())
            if message == "exit":
                clientSocket.close()
                exit(0)



if __name__ == "__main__":
    serverPort = 12000
    Client()


