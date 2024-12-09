import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.35"
        self.port = 5555
        self.address = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def getid(self):
        return self.id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            #return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
    
    
    def receive(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

    
