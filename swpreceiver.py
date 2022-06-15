import socket
import random
conn =socket.socket()
conn.connect(('localhost', 4444))
while True:
    err = random.random()
    data = conn.recv(1024)
    if not data:
        break
    d = data.decode()
    if d == 'END':
        break
    if round(err) == 0:
        print(d)
        conn.send("OK".encode())
    else:
        print("error",d,err)
        conn.send("ERR".encode())
conn.close()