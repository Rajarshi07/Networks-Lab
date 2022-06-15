import socket
parts = 10
s = socket.socket()
s.bind(('localhost', 4444))
s.listen()
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    i=1
    while i<=parts:
        data = "part " + str(i)
        conn.send(data.encode())
        ack = conn.recv(1024)
        if not ack:
            break
        if ack.decode()=='OK':
            print("sent",data)
            i+=1
        elif ack.decode()=='ERR':
            print("error: resending data",data)
            continue
    conn.send("END".encode())
    conn.close()