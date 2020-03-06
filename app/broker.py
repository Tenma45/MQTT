from socket import *
from threading import Thread
import os,sys
import pickle

SERV_PORT = 50000
ip = sys.argv[1]
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)

subDict = {}

def handle_client(s,addr):

    global subDict
    ip, port = str(addr[0]), str(addr[1])
    pack = s.recv(1024)
    data = pickle.loads(pack)
    role = data['role']
    topic = data['topic']
    message = data['message']

    if role=='publish':
        print('ip> %s:%s,' %(ip,port),'published on topic> %s,' %(topic),'message> %s' %(message))
        for node in subDict[topic]:
            node.send(message.encode('utf-8'))

    elif role=='subscribe':
        print('ip> %s:%s,' %(ip,port),'subscribe on topic> %s' %(topic))
        if topic in subDict.keys():
            subDict[topic].append(s)
        else:
            subDict[topic]=[s]
        while True:
            try:
                s.recv(1024)
            except:
                subDict[topic].remove(s)
                print(print('ip> %s:%s,' %(ip,port),'abandon on topic> %s' %(topic)))
                break

    s.close()
    return

while True:
    sckt, addr = s.accept()
    try:
        Thread(target=handle_client, args=(sckt,addr)).start()
    except:
        print("Cannot start thread..")
        import traceback
        trackback.print_exc() 