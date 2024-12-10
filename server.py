import socket
from _thread import *
import sys
import pickle
import time

server = "192.168.0.35"
port = 5555
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2)
print("waiting for connection")

move=[[0,1,1],[1,1,1]]
ready = [False,False]


def reset():
    move=[[0,1,1],[1,1,1]]
    ready = [False,False]


def threaded_client(conn, player):
    conn.send(pickle.dumps(player))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            print("some data", data,player)
            if not data:
                print("Disconnected")
                break
            elif data == [-1,-1,-1]:
                while ready[player] == False:
                    time.sleep(0.5)
                reply = move[(player+1)%2]
                ready[player] = False
                conn.sendall(pickle.dumps(reply))
                print("Sending : ", reply,player)
            elif data == [-2,-2,-2]:
                reset()
            elif player == data[0]%2:
                move[player] = data
                ready[(player+1)%2] = True
                print("Received: ", data)
        except:
            break

    print("Lost connection", player)
    reset()
    conn.close()



currentPlayer=0
while True:
    conn,addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer = (currentPlayer + 1)%2