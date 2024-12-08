import socket
from _thread import *
import sys
from engine import minimax,ThreadWithReturnValue


server = "192.168.0.35"
port = 5555

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for connection")

def threaded_client(connection):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            data = data.decode("utf-8")
            reply = ThreadWithReturnValue(target= minimax, args=data)
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    conn.close()

while True:
    conn,addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))