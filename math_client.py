import socket
def client():
    while True:
        sock = socket.socket()
        sock.connect(('localhost', 4444))
        data=input("Enter Expression to be evaluated: ")
        if(data=='EXIT'):
            return
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        sock.close()
client()