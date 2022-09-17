# # question 1
# from socket import *
# srvr=socket(AF_INET,SOCK_STREAM)
# srvr.bind(("localhost",3000))
# srvr.listen(5)
# t=srvr.accept()
# conn=t[0]
# print("server started")
# conn.send("hello from server".encode())
# received_message=conn.recv(1024)
# print(received_message)
# srvr.close()

# # question 2
# from socket import *
# srvr=socket(AF_INET,SOCK_STREAM)
# srvr.bind(("localhost",5000))
# srvr.listen(5)
# print("server started")
# t=srvr.accept()
# conn=t[0]
# received=conn.recv(1024)
# received=received.upper()
# received="%s"%received
# conn.send(received.encode())
# conn.close()
# srvr.close()

# # question 3
# from socket import *
# srvr=socket(AF_INET,SOCK_STREAM)
# srvr.bind(("localhost",5000))
# srvr.listen(5)
# print("server started")
# t=srvr.accept()
# conn=t[0]
# received=conn.recv(1024)
# if(received.decode()=="ping"):
#     received="pong"
#     print(received)
#     conn.send(received.encode())
# conn.close()
# srvr.close()

# # question 4
# from socket import *
# from threading import *
# srvr=socket(AF_INET,SOCK_STREAM)
# srvr.bind(("localhost",5000))
# srvr.listen(5)
# count=0
# print("server started")
# def hello(t,count):
#     conn=t[0]
#     received=conn.recv(1024)
#     received=received.decode()
#     received="message from thread%d is %s"%(count ,received)
#     conn.send(received.encode())
#     conn.close()
# while(True):
#     t=srvr.accept()
#     count+=1
#     t1=Thread(target=hello,args=(t,count))
#     t1.start()

# # question 5
# from socket import *
# from threading import *
# import time
# srvr=socket(AF_INET,SOCK_STREAM)
# srvr.bind(("localhost",5000))
# srvr.listen(5)
# print("server started")
# count=0
# def hello(count,*t):
#     conn=t[0]
#     received=conn.recv(1024)
#     received=received.decode()
#     print(received)
#     received="color"
#     conn.send(received.encode())
#     time.sleep(10)
#     while(True):
#         msg="turn %d"%count
#         ret="1"
#         conn.send(msg.encode())
#         msg=conn.recv(1024)
#         msg=msg.decode()
#         print(msg)
#         if(msg=="1"):
#             print("ok")
#         elif(msg=="0"):
#             print("illegal")
#         elif(msg=="checkmate"):
#             print("winner")
#             ret="0"
#             break
#         conn.send(ret.encode())
#     conn.close()
# while(True):
#     t=srvr.accept()
#     count+=1
#     t1=Thread(target=hello,args=(count,*t))
#     t1.start()

# # question 3
# from threading import *
# def hello_world(i):
#     print(f"hello from thread {i}")
# threadList=[]
# for i in range(1,51):
#     threaditems=Thread(target=hello_world,args=(i,))
#     threadList.append(threaditems)
# for i in range(1,51):
#     a=threadList.pop()
#     a.start()

# # question 4
# import threading
# arraysize=threading.Semaphore(5)
# availablesemaphore=5
# data=[]
# arrayemptylock=threading.Event()
# arrayfulllock=threading.Event()
# def producer():
#     global availablesemaphore
#     global data
#     for i in range(5):
#         if availablesemaphore==0:
#             arrayfulllock.wait()
#             arrayfulllock.clear()
#         arraysize.acquire()
#         data.append(i)
#         print(f"producer produced {i}")
#         availablesemaphore-=1
#         arrayemptylock.set()

# def consumer():
#     global availablesemaphore
#     global data
#     for i in range(5):
#         if availablesemaphore==5:
#             arrayemptylock.wait()
#             arrayemptylock.clear()
#         arraysize.release()
#         a=data.pop(0)
#         print(f"consumer consumed {a}")
#         availablesemaphore+=1
#         arrayfulllock.set()
# t1=threading.Thread(target=producer)
# t2=threading.Thread(target=consumer)
# t1.start()
# t2.start()

# # question 5
# import threading
# import time
# arraysize=threading.Semaphore(5)
# availablesemaphore=5
# data=[]
# mainlock=threading.RLock()
# arrayemptylock=threading.Event()
# arrayfulllock=threading.Event()
# def producer():
#     global availablesemaphore
#     global data
#     global mainlock
#     for i in range(5):
#         if availablesemaphore==0:
#             arrayfulllock.wait()
#             arrayfulllock.clear()
#         mainlock.acquire()
#         data.append(i)
#         print(f"producer produced {i}")
#         availablesemaphore-=1
#         mainlock.release()
#         time.sleep(5)
#         arrayemptylock.set()

# def consumer():
#     global availablesemaphore
#     global data
#     for i in range(5):
#         if availablesemaphore==5:
#             arrayemptylock.wait()
#             arrayemptylock.clear()
#         mainlock.acquire()
#         a=data.pop(0)
#         print(f"consumer consumed {a}")
#         availablesemaphore+=1
#         mainlock.release()
#         time.sleep(3)
#         arrayfulllock.set()
# t1=threading.Thread(target=producer)
# t2=threading.Thread(target=consumer)
# t1.start()
# t2.start()

# # question 6
# import sys
# import threading
# import time
# class Semaphore(object):
#     def __init__(self, initial):
#         self.lock = threading.Condition(threading.Lock())
#         self.value = initial
#     def up(self):
#         with self.lock:
#             self.value += 1
#             self.lock.notify()
#     def down(self):
#         with self.lock:
#             while self.value == 0:
#                 self.lock.wait()                 
#             self.value -= 1
# class ChopStick(object):
#     def __init__(self, number):
#         self.number = number           # chop stick ID
#         self.user = -1                 # keep track of philosopher using it
#         self.lock = threading.Condition(threading.Lock())
#         self.taken = False
#     def take(self, user):         # used for synchronization
#         with self.lock:
#             while self.taken == True:
#                 self.lock.wait()
#             self.user = user
#             self.taken = True
#             sys.stdout.write("p[%s] took c[%s]\n" % (user, self.number))
#             self.lock.notifyAll()
#     def drop(self, user):         # used for synchronization
#         with self.lock:
#             while self.taken == False:
#                 self.lock.wait()
#             self.user = -1
#             self.taken = False
#             sys.stdout.write("p[%s] dropped c[%s]\n" % (user, self.number))
#             self.lock.notifyAll()
# class Philosopher (threading.Thread):

#     def __init__(self, number, left, right, butler):
#         threading.Thread.__init__(self)
#         self.number = number            # philosopher number
#         self.left = left
#         self.right = right
#         self.butler = butler
#     def run(self):
#         for i in range(20):
#             self.butler.down()              # start service by butler
#             time.sleep(0.1)                 # think
#             self.left.take(self.number)     # pickup left chopstick
#             time.sleep(0.1)                 # (yield makes deadlock more likely)
#             self.right.take(self.number)    # pickup right chopstick
#             time.sleep(0.1)                 # eat
#             self.right.drop(self.number)    # drop right chopstick
#             self.left.drop(self.number)     # drop left chopstick
#             self.butler.up()                # end service by butler
#         sys.stdout.write("p[%s] finished thinking and eating\n" % self.number)
# def main():
#     n = 5
#     butler = Semaphore(n-1)
#     c = [ChopStick(i) for i in range(n)]
#     p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]
#     for i in range(n):
#         p[i].start()
# if __name__ == "__main__":
#     main()

# # question 7
# import threading as thread
# import random
# global x                #Shared Data
# x = 0
# lock = thread.Lock()    #Lock for synchronising access
# def Reader():
#     global x
#     print('Reader is Reading!')
#     lock.acquire()      #Acquire the lock before Reading (mutex approach)
#     print('Shared Data:', x)
#     lock.release()      #Release the lock after Reading
#     print()
# def Writer():
#     global x
#     print('Writer is Writing!')
#     lock.acquire()      #Acquire the lock before Writing
#     x += 1              #Write on the shared memory
#     print('Writer is Releasing the lock!')
#     lock.release()      #Release the lock after Writing
#     print()
# if __name__ == '__main__':
#     for i in range(0, 10):
#         randomNumber = random.randint(0, 100)   #Generate a Random number between 0 to 100
#         if(randomNumber > 50):
#             Thread1 = thread.Thread(target = Reader)
#             Thread1.start()
#         else:
#             Thread2 = thread.Thread(target = Writer)
#             Thread2.start()
# Thread1.join()
# Thread2.join()