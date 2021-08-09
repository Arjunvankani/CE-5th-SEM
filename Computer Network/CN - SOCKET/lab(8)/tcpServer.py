from socket import *
from json import *
from random import randint

host = 'localhost'
port = 4444

serversocket = socket(AF_INET,SOCK_STREAM,0)  #tcp
serversocket.bind((host,port))

serversocket.listen(2)  

con,adr = serversocket.accept()
print("Connection From:\t",adr)
Gid = {}   # gerate id 
while True:
    ch = con.recv(1024).decode()
    if int(ch) == 1:
        while True:
            val = con.recv(1024).decode()
            data = loads(val)
            
            strid = randint(1111,9999)
            Bid = "BOOK_ID" + str(strid)  #Booking Id
            Gid[Bid] = {}
            Gid[Bid].update({"Name":data[0]})
            Gid[Bid].update({"Pick up":data[1]})
            Gid[Bid].update({"Drop ":data[2]})
            
            keys = []
            for i in Gid.keys():
                keys.append(i)
            con.send(Bid.encode("utf-8"))
            brdata = con.recv(1024).decode()
            if(brdata == "yes"):
                True
            else:
                break
    if(int(ch)==2):
        keys = []
        for i in Gid.keys():
            keys.append(i)
        print(keys)
        while True:
            recdatacan = con.recv(1024).decode()
            if recdatacan in keys:
                del Gid[recdatacan]
                str = "0"
                con.send(str.encode("utf-8"))
                break
            else:
                str = "1"
                con.send(str.encode("utf-8"))
        #display data
    if(int(ch)==3):
        keys = []
        for i in Gid.keys():
            keys.append(i)
        while True:
            recdata = con.recv(1024).decode()
            if recdata in keys:
                templst = []
                for i in Gid[recdata].values():
                    templst.append(i)
                st = dumps(templst)
                con.send(st.encode("utf-8"))
                break
            else:
                str = "0"
                con.send(str.encode("utf-8"))
    if(int(ch) == 0):
        break
