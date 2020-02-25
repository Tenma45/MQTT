from socket import *
import sys

MAX_BUF = 2048
SERV_PORT = 50000
role = 'p'
ip = sys.argv[1]
topic = sys.argv[2]
data = sys.argv[3]
topicLength = str(len(topic)).zfill(2)
dataLength = str(len(data)).zfill(2)
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)
header =  role + topicLength + dataLength
payload = topic + data
pack = header + payload
# print(pack)
s.send(pack.encode('utf-8'))
print('Sent sucessfully')