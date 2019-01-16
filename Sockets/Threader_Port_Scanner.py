import threading
from queue import Queue
import socket

print_lock = threading.Lock()

target = 'pythonprogramming.net'

def pscan(port) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        con = s.connect((server), port)
        with print_lock :
            print('Port',port,'is open.')
        con.close()
    except :
        pass

def threader() :
    while True :
        worker = q.get()
        pscan(worker)
        q.task_done()

q = Queue()

#We create 30 threads or workers
for x in range(30) :
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

#We have 100 jobs to be done
for worker in range(1, 101) :
    q.put(worker)

q.join()
print('Done')
