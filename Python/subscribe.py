from socket import *
import sys
import pickle 

ip = sys.argv[1]
SERV_PORT = 50000
addr = (ip, SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)

if len(sys.argv)!=3:
    print('Invalid input')
else:
    s.connect(addr)
    data = {'role':'subscribe','topic':sys.argv[2],'message':''} #
    pack = pickle.dumps(data)   #เอาข้อมูลไป encode เพื่อให้ส่งได้
    s.send(pack)                #ส่ง pack ไปที่ให้ broker
    while True:
        message = s.recv(1024)  #รับข้อความจาก broker
        print ('message> %s' %(message.decode('utf-8'))) #โชว์ massege ที่ได้มาจาก broker 