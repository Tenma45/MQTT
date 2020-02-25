from socket import *
from threading import Thread
import os,sys

SERV_PORT = 50000
ip = sys.argv[1]
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)
counter = 0
counterDict = {}
publishData = False
publishTopic = False

def handle_client(s,ip,port):
    global publishData
    global publishTopic
    global counterDict
    global counter
    packRaw = s.recv(1024)
    pack = packRaw.decode('utf-8')
    role = pack[0]
    if role=='p':
        topicLength = int(pack[1:3])
        dataLength = int(pack[3:5])
        topic = pack[5:5+topicLength]
        data = pack[5+topicLength:5+topicLength+dataLength]
        while publishData!=False:
            pass
        print('ip> %s:%s,' %(ip,port),'published on topic> %s,' %(topic),'message> %s' %(data))
        if topic not in counterDict.keys():
            counter = 0
        else:
            counter = counterDict[topic]
        publishTopic = topic
        publishData = data
        while counter!=0:
            # print(counter)
            pass
        publishTopic = False
        publishData = False
    elif role=='s':
        topicLength = int(pack[1:3])
        topic = pack[3:3+topicLength]
        if topic in counterDict.keys():
            counterDict[topic]+=1
        else:
            counterDict[topic]=1
        # print('counterDict> '+str(counterDict))
        print('ip> %s:%s,' %(ip,port),'subscribe on topic> %s' %(topic))
        while True:
            while publishTopic!=topic:
                pass
            counter = counter-1
            try:
                s.send(publishData.encode('utf-8'))
            except:
                counterDict[topic] = counterDict[topic]-1
                break
            while publishTopic==topic:
                pass
    s.close()
    return

while True:
    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1])
    try:
        Thread(target=handle_client, args=(sckt,ip,port)).start()
    except:
        print("Cannot start thread..")
        import traceback
        trackback.print_exc()