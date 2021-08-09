from socket import *
from time import *

host = 'localhost'
port = 4444

socketserver = socket(AF_INET,SOCK_DGRAM) # UDP
ip = (host,port)
lst = []
seq = 10
i = 0
while i < seq:
    i += 1
    srttime = time()
    socketserver.sendto(str(i).encode("utf-8"),ip)
    rec = socketserver.recvfrom(1024)
    rtt = time() - srttime
    tm = localtime(rtt)
    lst.append(tm.tm_sec)
    if(tm.tm_sec <=1):
        print("Responce from server with in.......",tm.tm_sec)
    else:
        print("Responce time out......")
    sleep(0.5)
print("All timing for response",lst)
n1 = sum(lst)
n2 = len(lst)
avg = n1/n2
print("Totle RTT Time",str(n1))
print("Maximum RTT Time",str(max(lst)))
print("Minimum RTT Time",str(min(lst)))
print("Average RTT Time",str(avg))
