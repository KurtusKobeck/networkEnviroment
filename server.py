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
            print("client: " + str(message[1:]))
            reply = self.processMessage(message)
            print("server: " + str(reply[1:]))
            client.send(reply.encode())                   #Sends the client terminal str(response)
    def processMessage(self, message):
        #A message must include both an "origin tag" and it's contents.
        #Even null content messages will transmit to client a response of it's origin tag in a tuple.
        #Supported psuedo-commands:
        #Empty  - "0"
        #Mul    - "M"
        #Echo   - "E"
        #Null   - "N"
        message=message[1:]
        if len(message) == 0:
            return "E"+"Empty command received from client."
        if ("echo" in message):
            if (message[0:4] == "echo"):
                return "E"+message[5:]
        if ("mul" in message):
            if (message[0:3] == "mul"):
                spacelessMessage=message[3:].replace(" ","")
                if (spacelessMessage.isnumeric()):
                    return "M"+str(int(spacelessMessage)*2)
                dashlessMessage = spacelessMessage.replace("-","")
                if (dashlessMessage.isnumeric()):
                    return "M"+str(int(dashlessMessage)*-2)
        return "N"

if __name__ == '__main__':
    server = server(socket.gethostname(),1234)  #Initialize the server
