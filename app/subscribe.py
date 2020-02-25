from socket import *
import sys
MAX_BUF = 2048
SERV_PORT = 50000
role = 's'
ip = sys.argv[1]
topic = sys.argv[2]
topicLength = str(len(topic)).zfill(2)
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)
header =  role + topicLength
payload = topic
pack = header + payload
s.send(pack.encode('utf-8'))
while True:
    message = s.recv(2048)
    print ('message> %s' %(message.decode('utf-8')))