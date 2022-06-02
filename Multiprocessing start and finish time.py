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

output:
Program finished in 0.025785300007555634 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Finished sleeping
Finished sleeping
