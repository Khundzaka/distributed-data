# This is optional extra information. Not required to learn
# This code is unfinished, might not run.

import datetime
from multiprocessing import Process

# Define a function for the thread
def print_time( threadName):
    dt = datetime.datetime.now()
    count = 0
    while count < 100_000_000:
      count += 1
    #   print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
    print (threadName, "finished Execution after", datetime.datetime.now() - dt)

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1",) )
#    _thread.start_new_thread( print_time, ("Thread-2",) )
#    _thread.start_new_thread( print_time, ("Thread-3",) )
#    _thread.start_new_thread( print_time, ("Thread-4",) )
# except:
#    print ("Error: unable to start thread")

# while 1:
#    pass

if __name__ == '__main__':
    p = Process(target=print_time, args=('Thread-1', ))
    p2 = Process(target=print_time, args=('Thread-2', ))
    p3 = Process(target=print_time, args=('Thread-3', ))
    p4 = Process(target=print_time, args=('Thread-4', ))
    p.start()
    p2.start()
    p3.start()
    p4.start()