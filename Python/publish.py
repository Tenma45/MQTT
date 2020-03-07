from socket import *
import sys
import pickle

ip = sys.argv[2] 
SERV_PORT = 50000 
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)

if len(sys.argv)!=5:
    print('Invalid input')
else:
    s.connect(addr)
    data = {'role':'publish','topic':sys.argv[3],'message':sys.argv[4]} 
    pack = pickle.dumps(data) 
    s.send(pack)
    print('Sent sucessfully')