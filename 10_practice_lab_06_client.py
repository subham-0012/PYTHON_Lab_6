# # question 1
# from socket import *
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",3000))
# print("client started")
# recvd=clnt.recv(1024)
# print(recvd)
# clnt.send("hello from client".encode())
# clnt.close()

# # question 2
# from socket import *
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",5000))
# print("enter the message")
# message1=input()
# clnt.send(message1.encode())
# received=clnt.recv(1024)
# print("message received")
# print(received)
# clnt.close()

# # question 3
# from socket import *         
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",5000))
# print("enter the message")
# message1=input()
# clnt.send(message1.encode())
# received=clnt.recv(1024)
# print(received.decode())
# clnt.close()

# # question 4
# from socket import *
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",5000))
# print("enter the message")
# message1=input()
# clnt.send(message1.encode())
# received=clnt.recv(1024)
# print(received.decode())
# clnt.close()
# from socket import *
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",5000))
# print("enter the message")
# message1=input()
# clnt.send(message1.encode())
# received=clnt.recv(1024)
# print(received.decode())
# clnt.close()

# # question 5
# from socket import *
# import time
# clnt=socket(AF_INET,SOCK_STREAM)
# clnt.connect(("localhost",5000))
# print("enter handle")
# message1=input()
# clnt.send(message1.encode())
# received=clnt.recv(1024)
# print(received.decode())
# while(True):
#     inp=input("enter your move 1")
#     clnt.send(inp.encode())
#     ret=clnt.recv(1024)
#     ret=ret.decode()
#     if(ret=="0"):
#         break
#     time.sleep(5)
# clnt.close()

# from socket import *
# import time
# clnt1=socket(AF_INET,SOCK_STREAM)
# clnt1.connect(("localhost",5000))
# print("enter handle")
# message2=input()
# clnt1.send(message2.encode())
# received=clnt1.recv(1024)
# print(received.decode())
# while(True):
#     inp=input("enter your move 2")
#     clnt1.send(inp.encode())
#     ret1=clnt1.recv(1024)
#     ret1=ret1.decode()
#     if(ret1=="0"):
#         break
#     time.sleep(5)
# clnt1.close()
