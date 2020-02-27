from socket import *
import sys
import pickle

MAX_BUF = 2048
SERV_PORT = 50000
ip = sys.argv[1]
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

data = {'role':'publish','topic':sys.argv[2],'data':sys.argv[3]}
pack = pickle.dumps(data)
s.send(pack)

print('Sent sucessfully')