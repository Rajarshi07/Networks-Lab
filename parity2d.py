def printTable(l,word):
    for i in range(len(l)):
        if i==len(l)-1:
            print('_'*(len(l[0])*2+7))
            print('   ',' '.join(l[i][:-1]),' | ',l[i][-1])
            continue
        print(word[i],' ',' '.join(l[i][:-1]),' | ',l[i][-1])
    print()

def parity2d(word,showTable=True):
    w = word.encode('ascii')
    l=[]
    for i in w:
        b = "{0:08b}".format(int(i))
        c=0
        for j in b:
            if j=='1':
                c+=1
        if c%2==0:
            b+='0'
        else:
            b+='1'
        l.append(b)
    cpb = ''
    for i in range(len(l[0])):
        c = 0
        for j in range(len(l)):
            if(l[j][i]=='1'):
                c+=1
        if(c%2==0):
            cpb+='0'
        else:
            cpb+='1'
    l.append(cpb)
    if showTable:
        printTable(l,word)
    return ''.join(l).encode()


print(parity2d("HELLO"))