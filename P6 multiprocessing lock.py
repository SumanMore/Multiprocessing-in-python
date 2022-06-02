
'''
What Are The Locks Used For In Multiprocessing In Python?
The lock is used for locking the processes while using multiprocessing in Python. With its acquire() and release() methods, you can lock and resume processes. 
Thus, it allows you to execute specific tasks based on priority while stopping the other processes.'''

'''When we want that only one process is executed at a time in that situation Locks is use. 
That means that time blocks other process from executing similar code.
Lock will be released after the process gets completed.'''
 
#when two process wants to access the same shared memory/files/database simultaneously it ctreates a problem thats'y to encounter this ptoblem we use lock#    
    
import time
import multiprocessing

#first process is depositing money in the back
def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        #below 3 lines are crtical section part
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

#second process is withdrawing money from the back
def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance,lock))
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value) #prints the final balance

  '''
  output
  200
  '''
