
from socket import *
import threading
import time
import sys

class Server():

    def listenToClient(self, client, addr, clients_list):

        while True:

            message = client.recv(1024)
            if message == "exit":
                print (addr, " is closed")
                client.close()
                exit(0)
            else:
                print (addr, " : ", message.decode("utf-8"),time.strftime("%H:%M:%S"))

            for clients in clients_list:
                if clients != client:
                    clients.send(message)



    def __init__(self, serverPort):

        try:
            serverSocket = socket(AF_INET, SOCK_STREAM)
        except:
            print ("Socket cannot be created!!!")
            exit(1)
        print ("Socket is created...")

        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
            print ("Socket cannot be used!!!")
            exit(1)
        print ("Socket is being used...")

        try:
            serverSocket.bind(('', serverPort))
        except:
            print ("Binding cannot de done!!!")
            exit(1)
        print ("Binding is done...")

        try:
            serverSocket.listen(45)
        except:
            print ("Server cannot listen!!!")
            exit(1)
        print ("The server is ready to receive")
        clients_list =[]

        while True:
            connectionSocket, addr = serverSocket.accept()
            clients_list.append(connectionSocket)

            threading.Thread(target=self.listenToClient, args=(connectionSocket, addr, clients_list)).start()

if __name__ == "__main__":
    serverPort = 12000
    Server(serverPort)

