import socket
from threading import Thread
import sys

c = socket.socket()
c.connect(('localhost', 9000))
kill=False
def recvthread(arg1,sock):
    global kill
    print('receiver init')
    while True:
        if(kill):
            return
        try:
            print(sock.recv(1024).decode())
        except:
            pass

def sendthread(sock):
    global kill
    while True:
        txt = input()
        sock.send(txt.encode())
        if(txt=='BYE'):
            kill=True
            sock.close()
            return

Thread(target=recvthread,args=('t',c)).start()
sendthread(c)

