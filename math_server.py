import socket
from math import sqrt
s = socket.socket()
s.bind(('localhost', 4444))
s.listen()
while(1):
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    exp = data.decode()
    try:
        out = eval(exp)
    except:
        out = 'Invalid Expression'
    conn.sendall(str(out).encode())
    conn.close()