def xor(a,key):
    o = '{:016b}'.format(int(a,2)^int(key,2))[-(len(key)-1):]
    return o

def mod2div(s,k):
    l = len(k)    
    t = s[:l-1]
    for i in range(len(s)-len(k)+1):
        t+=s[l+i-1]
        if(t[0]=='0'):
            t=xor(t, '0'*l)
        else:
            t=xor(t, k)
    return t

def CRCencode(send,key):
    l = len(key)
    s = send+'0'*(l-1)
    r = mod2div(s, key)
    return send+r

def CRCdecode(recv,key):
    l = len(key)
    r = mod2div(recv, key)
    if(int(r)==0):
        return recv[:-(l-1)]
    else:
        return False

send = "11010011101100"
key = "1011"
recv = CRCencode(send, key)
print(recv)
print(CRCdecode(recv, key))
print(CRCdecode('0'+recv[1:], key)) #incorrect recv check