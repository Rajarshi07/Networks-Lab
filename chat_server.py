import socket
from threading import Thread
from queue import Queue

s = socket.socket()
print('Socket created')
s.bind(('localhost', 9000))
s.listen()
conns = {}
print('Waiting for connection')
chatqueue = Queue()

def chatlistener(conn,addr,chatqueue):
    try:
        print('Connected by', addr)
        while True:
            rv = conn.recv(1024)
            txt = rv.decode()
            print(addr,':',txt)
            chatqueue.put_nowait([f'({addr[0]}:{str(addr[1])}) : {txt}',addr])
            if(txt=='BYE'):
                conns.pop(addr)
                conn.close()
                return 0
    except ConnectionResetError:
        return 0

def send_chat(conns,chaqueue):
    while True:
        if(len(conns)==0):
            continue
        try:
            msg = chatqueue.get(timeout=3)
            for k,v in conns.items():
                if(k!=msg[1]):
                    try:
                        v.send(msg[0].encode())
                    except:
                        pass
        except Exception as e:
            # print(e)
            pass
        
            

Thread(target=send_chat,args=(conns,chatqueue)).start()
while True:
    conn, addr = s.accept()
    conns[addr] = conn
    Thread(target=chatlistener,args=(conn,addr,chatqueue)).start()

