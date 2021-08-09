from socket import *
from json import *

host = 'localhost'
port = 4444

socketclient = socket(AF_INET,SOCK_STREAM,0)  #Tcp
socketclient.connect((host,port))

F = 1
while F == 1:
    print("Welcome to our Airline Service 24*7 \n")
    ans = int(input("\t 1) For Booking Your Ticket: \n\t 2) Process to cancle ticket\n\t 3)History & Cheking Conformation ticket: \n \t 0.Exit\n\t Enter Your choices :\t "))
    socketclient.send(str(ans).encode("utf-8"))
    if(ans == 1):
        while True:
            lst = []
            lst.append(input("Enter Your Name:"))
            lst.append(input("Enter Your Pick up:"))
            lst.append(input("Enter Your Drop:"))
            
            senddata = dumps(lst)
            
            socketclient.send(senddata.encode("utf-8"))
            id=socketclient.recv(1024).decode()
            
            print("Your Booking is Conform And Booking Id Is:",id)
            agindata = input("Do you want to book another Ticket ?\n \t  [yes/no]:")
            socketclient.send(agindata.encode("utf-8"))
            if(agindata == "yes"):
                True
            else:
                break
    if(ans == 2):
        while True:
            getid = input("Enter Your Booking Id:")
            socketclient.send(getid.encode("utf-8"))
            recdata = socketclient.recv(1024).decode()
            if (recdata != "1"):
                print("Your ticket cancle")
                break
            else:
                print("Maybe you type wrong Id or You don't book ticket right now!!")
                break
    if(ans == 3):
        while True:
            getid = input("Enter Your Booking Id:")
            socketclient.send(getid.encode("utf-8"))
            recdata=socketclient.recv(1024).decode()
            if(recdata != "0"):
                ans = loads(recdata)
                print("Booking Conform:")
                print("Your Booking id is:",getid)
                print("Your Name is:",ans[0])
                print("Your Source address:", ans[1])
                print("Your Destination address:", ans[2])
                break
            else:
                print("Maybe you type wrong Id or You don't book ticket right now!!")
    if(ans == 0):
        F = 0
