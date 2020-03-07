from socket import *
from threading import Thread
import os,sys
import pickle

ip = sys.argv[1]        #เก็บ arg ตัวที่ 1 ไว้ใน ip
SERV_PORT = 50000       #set port
addr = (ip, SERV_PORT)  #เอา ip กับ port มาต่อกัน
s = socket(AF_INET, SOCK_STREAM) #สร้าง socket TCP
s.bind(addr)            #bind socket กับ address
s.listen(1)             #รับ connection ได้ทีละ 1 connection/thread

subscribeList = {}      #สร้าง subcriber list เป็นแบบ dict (key เป็นชื่อ topic, value เป็น list ของ socket)

def handle_subscribe(sckt,ip,port,topic): #ฟังก์ชันรับ Thread ของ subscribe

    global subscribeList    #ประกาศให้ใช้ subscribeList แบบ global

    print('ip> %s:%s,' %(ip,port),'subscribe on topic> %s' %(topic))    #โชว์ว่า ip และ port นี้กำลัง subscribe topic ไหน
    if topic in subscribeList.keys():       #ถ้า topic อยู่ใน list
        subscribeList[topic].append(sckt)   #เพิ่ม socket ใน list
    else:
        subscribeList[topic]=[sckt]     #ถ้ายังไม่มี จะให้ socket นั้นเป็นตัวแรกใน list
    while True:     #วนเช็ค subscriber ยังอยู่
        try:
            sckt.recv(1024)     #เช็คว่า client subscriber ยังรันอยู่
        except:
            subscribeList[topic].remove(sckt)   #ลบ socket ของ subscriber ออก
            print('ip> %s:%s,' %(ip,port),'unsubscribe on topic> %s' %(topic)) #โชว์ว่า unsubscribe
            sckt.close()    #ปิด socket
            return
    
while True:

    sckt, addr = s.accept() #รับ connection 
    ip, port = str(addr[0]), str(addr[1]) #เอา addr ที่ได้จากตอนรับมาจาก client มาเก็บไว้ที่ ip กับ port
    pack = sckt.recv(1024)  #รอรับ pack จาก client
    data = pickle.loads(pack)   #decode pack ให้เป็น object
    role = data['role']         #เอา value ส่วนของ role มาเก็บ
    topic = data['topic']       #เอา value ส่วนของ topic มาเก็บ
    message = data['message']   #เอา value ส่วนของ messege มาเก็บ

    if role == 'publish':   #เช็ค role publish
        print('ip> %s:%s,' %(ip,port),'published on topic> %s,' %(topic),'message> %s' %(message)) #โชว์ข้อความว่า publish จากใคร topic ไหน
        for node in subscribeList[topic]:   #วนส่ง value(socket) ใน list ของ topic นั้น
            node.send(message.encode('utf-8'))    
        sckt.close()

    elif role == 'subscribe':   #เช็ค role subscribe
        try:
            Thread(target=handle_subscribe, args=(sckt,ip,port,topic)).start()
        except:
            print("Cannot start thread..")
            import traceback
            trackback.print_exc() 