import socket
from threading import Thread

class server:
        def __init__(self, HOST, PORT):
            print("Server initialized.")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((HOST,PORT))
            self.socket.listen(5)
            self.awaitConnection()
        def awaitConnection(self):
            while True:
                client, address = self.socket.accept()
                print("Client has connected.")
                Thread(target = self.processClient, args = (client,)).start()
        def processClient(self, client):
            while True:
                try:
                    message = client.recv(2048).decode()        #Received client input...
                except ConnectionResetError as e:
                    if e.errno == 10054:                        #This handles the client closing their terminal
                        print("Client terminal closed.")
                        client.close()
                        return                                  #This will terminate the thread.
                #process message here!
                print("client: " + str(message))
                reply = self.processMessage(message)
                print("server: " + str(reply))
                client.send(reply.encode())                   #Sends the client terminal str(response)
        def processMessage(self, message):
            response = ""
            if len(message) == 0:
                return "Empty command received from client."
            return response
if __name__ == '__main__':
    server = server(socket.gethostname(),1234)  #Initialize the server
