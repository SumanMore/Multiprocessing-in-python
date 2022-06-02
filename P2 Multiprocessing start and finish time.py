import multiprocessing
import time
 
def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')
 
if __name__ == "__main__":
    start_time = time.perf_counter()
 
    # Creates two processes
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
 
    # Starts both processes
    p1.start()
    p2.start()
 
    finish_time = time.perf_counter()
 
    print(f"Program finished in {finish_time-start_time} seconds")
  
 '''We must fence our main program under if __name__ == "__main__" or otherwise the multiprocessing module will complain. 
 This safety construct guarantees Python finishes analyzing the program before the sub-process is created.'''
'''
output:
Program finished in 0.025785300007555634 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Finished sleeping
Finished sleeping

However, there is a problem with the code, as the program timer is printed before the processes we created are even executed. 
We need to call the join() function on the two processes to make them run before the time prints. 
This is because three processes are going on: p1, p2, and the main process. The main process is the one that keeps track of the time
and prints the time taken to execute. We should make the line of finish_time run no earlier than the processes p1 and p2 are finished. 
We just need to add this snippet of code immediately after the start() function calls:
'''
import multiprocessing
import time
 
def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')
 
if __name__ == "__main__":
    start_time = time.perf_counter()
 
    # Creates two processes
    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)
 
    # Starts both processes
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish_time = time.perf_counter()
 
    print(f"Program finished in {finish_time-start_time} seconds")
  
'''  
OUTPUT:
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Finished sleeping
Finished sleeping
Program finished in 0.673008400015533 seconds
'''
