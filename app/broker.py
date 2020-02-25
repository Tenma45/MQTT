from socket import *
from threading import Thread
import os,sys
import time

SERV_PORT = 50000
ip = sys.argv[1]
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(1)
# subscribers = []
publishData = False
publishTopic = False

def handle_client(s,port):
    global publishData
    global publishTopic
    packRaw = s.recv(1024)
    pack = packRaw.decode('utf-8')
    role = pack[0]
    if role=='p':
        topicLength = int(pack[1:3])
        dataLength = int(pack[3:5])
        topic = pack[5:5+topicLength]
        data = pack[5+topicLength:5+topicLength+dataLength]
        publishData = data
        publishTopic = topic
        print('published on topic> %s,' %(topic),'message> %s' %(data))
    if role=='s':
        topicLength = int(pack[1:3])
        topic = pack[3:3+topicLength]
        print('subscribe on topic> %s' %(topic))
        while True:
            while publishTopic!=topic:
                pass
            s.send(publishData.encode('utf-8'))
            time.sleep(1)
            publishTopic=False
    s.close()
    return

while True:
    sckt, addr = s.accept()
    ip, port = str(addr[0]), str(addr[1])
    print ('New client connected from ..' + ip + ':' + port)
    try:
        Thread(target=handle_client, args=(sckt,port)).start()
    except:
        print("Cannot start thread..")
        import traceback
        trackback.print_exc()