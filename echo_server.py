import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 4444))
s.listen()
while(1):
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    print(data.decode())
    conn.sendall(data)
    conn.close()