
The multiprocessing package supports spawning processes. It refers to a function that loads and executes a new child processes. 
For the child to terminate or to continue executing concurrent computing,then the current process hasto wait using an API, 
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



Example 2:
We can also pass arguments to the function using args keyword.
In this example, we create two process that calculates the cube and squares of numbers and prints all results to the console.

import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square ' + str(n*n))

def calc_cube(numbers):
    for n in numbers:
        print('cube ' + str(n*n*n))

if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,)) #creates process p1
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))  #creates the process p2

    p1.start() #it will start the process p1
    p2.start()  #it will start the process p2

    p1.join()  #it will wait until the execution of this process is over
    p2.join()

    print("Done!")
   
We can also create more than one process at atime.
In this example, at first we create one process which is process1, this process just calculates the square of a number and at the same
time second process process2 is calculates the cube of a number.

