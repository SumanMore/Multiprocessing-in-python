import multiprocessing
import os
  
def worker1():
    # printing process id
    print("ID of process running worker1: {}".format(os.getpid()))
  
def worker2():
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))
  
if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))
  
    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)
  
    # starting processes
    p1.start()
    p2.start()
  
    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))
  
    # wait until processes are finished
    p1.join()
    p2.join()
  
    # both processes finished
    print("Both processes finished execution!")
  
    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))
    
    
    '''
    output
ID of main process: 28628
ID of process running worker1: 29305
ID of process running worker2: 29306
ID of process p1: 29305
ID of process p2: 29306
Both processes finished execution!
Process p1 is alive: False
Process p2 is alive: False
'''
    '''he main python script has a different process ID and multiprocessing module spawns new processes with different process IDs as we create Process objects p1 and p2. In above program, we use os.getpid() function to get ID of process running the current target function.
Notice that it matches with the process IDs of p1 and p2 which we obtain using pid attribute of Process class.

Each process runs independently and has its own memory space.
As soon as the execution of target function is finished, the processes get terminated. In above program we used is_alive method of Process class to check if a process is still active or not.
'''
