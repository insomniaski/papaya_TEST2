import threading
import threadpool
import time
def request():
    print 'start'
    time.sleep(5)
    print 'end'

threads=[]
t1=threading.Thread(target=request)
t2=threading.Thread(target=request)
threads.append(t1)
threads.append(t2)

count=0

for t in threads:
    #t.setDaemon(True)
    t.start()
