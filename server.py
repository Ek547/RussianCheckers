import socket
from _thread import *
import sys
import pickle


server = "192.168.0.35"
port = 5555
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2)
print("waiting for connection")

move=[[0,0,0],[1,1,1]]
ready = False





def threaded_client(conn, player):
    conn.send(pickle.dumps(player))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            if not data:
                print("Disconnected")
                break
            else:
                if player == data[0]%2:
                    move[player] = data
                    ready = True
                    print("Received: ", data)
                else:
                    if ready == True:
                        reply = move[(player+1)%2]
                        ready = False
                        conn.sendall(pickle.dumps(reply))
                        print("Sending : ", reply)
        except:
            break

    print("Lost connection")
    conn.close()



currentPlayer=0
while True:
    conn,addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer = (currentPlayer + 1)%2