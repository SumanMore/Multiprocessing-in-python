import time
import multiprocessing
def task():
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')
 
if __name__ == "__main__": 
    start_time = time.perf_counter()
    processes = []
 
    # Creates 10 processes then starts them
    for i in range(10):
        p = multiprocessing.Process(target = task)
        p.start()
        processes.append(p)
    
    # Joins all the processes 
    for p in processes:
        p.join()
 
    finish_time = time.perf_counter()
 
    print(f"Program finished in {finish_time-start_time} seconds")
  
''' 
Output:
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Sleeping for 0.5 seconds
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Finished sleeping
Program finished in 0.7548606999916956 seconds
'''
  
