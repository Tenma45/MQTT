from socket import *
import sys
import pickle 

ip = sys.argv[1]
SERV_PORT = 50000
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

data = {'role':'subscribe','topic':sys.argv[2],'message':''}
pack = pickle.dumps(data)
s.send(pack)

while True:
    message = s.recv(1024)
    print ('message> %s' %(message.decode('utf-8')))