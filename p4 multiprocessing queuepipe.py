'''
What Are the Queues Used For In Multiprocessing In Python?
The Queue in Python is a data structure based on the FIFO (First-In-First-Out) concept.queue helps in communication between different processes
in multiprocessing in Python. It provides the put() and get() methods to add and receive data from the queue. 
'''

#sharing data between processes using queue
#When we pass data between processes then at that time we can use Queue object.

import multiprocessing

def calc_square(numbers, q): #child process
    for n in numbers:
        q.put(n*n) #inserting data at the end of the queue

if __name__ == "__main__": #parent process
    numbers = [2,3,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get()) #iterating through queue and printing the elements
        
        
'''In this example, at first create a function that cal square of a number and inserting in the queue
Then we create a queue object and a process object then we start the process.
And finally check whether the queue is empty or not.
When we print the numbers, at first we print the value which is in front of the queue then next one and so on.
'''
'''
output
4
9
25
'''

