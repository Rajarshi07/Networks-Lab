import time
import socket
s = socket.socket()
print('Socket created')
s.bind(('localhost', 4444))
s.listen()
print('Waiting for connection')
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    conn.send(time.ctime().encode())

