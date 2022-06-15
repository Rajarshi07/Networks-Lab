#!/usr/bin/env python
# coding: utf-8

# In[84]:


def getClass(ip):
    ip = ip.split('/')
    if len(ip)==2:
        return 'CIDR',int(ip[-1])
    parts=list(map(int,ip[0].split('.')))
    if parts[0]>=0 and parts[0]<=127:
        return 'A',8
    elif parts[0]>=128 and parts[0]<=191:
        return 'B',16
    elif parts[0]>=192 and parts[0]<=223:
        return 'C',24
    elif parts[0]>=224 and parts[0]<=239:
        return 'D',32
    elif parts[0]>=240 and parts[0]<=255:
        return 'E',32
    else:
        return 'Invalid',0


# In[85]:


def getMask(suffix):
    if(suffix>32 or suffix<0):
        return False
    m = '1'*suffix+'0'*(32-suffix)
    parts = [m[i:i+8] for i in range(0, len(m), 8)]
    subnetMask = []
    for part in parts:
        subnetMask.append(str(int(part,2)))
    return '.'.join(subnetMask)


# In[86]:


def isValid(ip):
    ip = ip.split('/')[0]
    parts = list(map(int,ip.split('.')))
    if len(parts)!=4:
        return False
    for part in parts:
        if part < 0 or part > 255:
            return False
    return True


# In[87]:


def getIpDetails(ip):
    if not isValid(ip):
        return "Invalid IP Address"
    ipClass = getClass(ip)
    subnet = getMask(ipClass[1])
    subnetParts = list(map(int,subnet.split('.')))
    ip = ip.split('/')[0]
    parts = list(map(int,ip.split('.')))
    netId = []
    for i in range(len(parts)):
        netId.append(subnetParts[i]&parts[i])
    netId = '.'.join(map(str,netId))
    return ipClass[0],subnet,netId


# In[88]:


ips = [
    '112.56.75.10',
    '213.10.0.5',
    '197.57.10.10',
    '132.75.75.1',
    '256.10.175.9',
    '233.10.5.10',
    '124.50.26.10/24',
    '124.50.26.10/27',
    '124.50.26.10/10',
    '142.256.0.22/12'
]
for ip in ips:
    print(ip,getIpDetails(ip))


# In[89]:


import socket


# In[90]:


host = socket.gethostname()
ip = socket.gethostbyname(host)
print(host,ip,getNetwork(ip))

