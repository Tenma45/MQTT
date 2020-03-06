from socket import *
import sys
import pickle

ip = sys.argv[1] 
SERV_PORT = 50000 
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

data = {'role':'publish','topic':sys.argv[2],'message':sys.argv[3]} 
pack = pickle.dumps(data) 
s.send(pack)

print('Sent sucessfully')