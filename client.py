import socket
from threading import Thread
import os

class Client:
    def __init__(self, HOST, PORT):
        self.socket=socket.socket()
        self.socket.connect((HOST,PORT))
        #Thread(target = self.receiveResponseLoop).start()
        self.sendCommandLoop()
    def sendCommandLoop(self):
        while True:
            clientCommand = "0"+input("Enter your command: ")
            self.socket.send(clientCommand.encode())
            self.receiveResponseLoop()
    def receiveResponseLoop(self):
        while True:
            serverResponse = self.socket.recv(2048).decode()
            if not serverResponse:
                of._exit(0)
            if len(serverResponse)>1:
                print(serverResponse[1:])
            return
if __name__ == '__main__':
    Client(socket.gethostname(), 1234)
