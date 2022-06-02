The multiprocessing package supports spawning processes. It refers to a function that loads and executes a new child processes. 
For the child to terminate or to continue executing concurrent computing,then the current process has to wait using an API, 
which is similar to threading module.
When we work with Multiprocessing,at first we create process object. Then it calls a start() method.

Example-1:
   from multiprocessing import Process
   def display():
      print ('Hi !! I am Python')
      if __name__ == '__main__':
      p = Process(target=display)
      p.start()
      p.join()
In this example, at first we import the Process class then initiate Process object with the display() function.
Then process is started with start() method and then complete the process with the join() method.



Example-2:
import time
import multiprocessing
def task():
    print("hello before sleeping")
    time.sleep(0.5) #sleeping for 0.5s
    print("hello after sleeping")
if __name__ == "__main__":   
     p1=multiprocessing.Process(target=task)
     p1.start()
     print("done")


Output:
done
hello before sleeping
hello after sleeping
