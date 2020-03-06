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

subscribeList = {}

def handle_subscribe(sckt,ip,port,topic):

    global subscribeList

    print('ip> %s:%s,' %(ip,port),'subscribe on topic> %s' %(topic))
    if topic in subscribeList.keys():
        subscribeList[topic].append(sckt)
    else:
        subscribeList[topic]=[sckt]
    while True:
        try:
            sckt.recv(1024)
        except:
            subscribeList[topic].remove(sckt)
            print('ip> %s:%s,' %(ip,port),'unsubscribe on topic> %s' %(topic))
            sckt.close()
            return
    
while True:

    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1])
    pack = sckt.recv(1024)
    data = pickle.loads(pack)
    role = data['role']
    topic = data['topic']
    message = data['message']

    if role == 'publish':
        print('ip> %s:%s,' %(ip,port),'published on topic> %s,' %(topic),'message> %s' %(message))
        for node in subscribeList[topic]:
            node.send(message.encode('utf-8'))
        sckt.close()

    elif role == 'subscribe':
        try:
            Thread(target=handle_subscribe, args=(sckt,ip,port,topic)).start()
        except:
            print("Cannot start thread..")
            import traceback
            trackback.print_exc() 