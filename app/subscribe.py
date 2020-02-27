from socket import *
import sys
import pickle 

MAX_BUF = 2048
SERV_PORT = 50000
ip = sys.argv[1]
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

data = {'role':'subscribe','topic':sys.argv[2],'data':''}
pack = pickle.dumps(data)
s.send(pack)

while True:
    message = s.recv(2048)
    print ('message> %s' %(message.decode('utf-8')))