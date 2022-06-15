import socket
c = socket.socket()
c.connect(('localhost', 4444))
data="hello from client"
c.send(data.encode())
print(c.recv(1024).decode())