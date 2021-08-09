from socket import *
from time import sleep

host = 'localhost'
port = 4444

socketserver = socket(AF_INET,SOCK_DGRAM)  #UDP
socketserver.bind((host,port))

data = []

for i in range(10):
    value = socketserver.recvfrom(1024)
    ip = value[1]
    
    data.append(value[0].decode())
    if data[i] == "3" or data[i] == "6":
        sleep(3)
    send = socketserver.sendto(data[i].encode(),ip)
    sleep(2)
print("Connection Address of server:",ip)
