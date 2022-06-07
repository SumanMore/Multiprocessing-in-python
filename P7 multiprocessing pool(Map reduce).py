'''
Pool module represents a pool of worker processes.
Pool of worker

It hides the complexity of concurrency programing.

- You do not have to worry about managing processes or shared data or stats between workers.

- You do not have to worry about distributing the work between workers. Ι

- All you need to do is :

• Create pool of X processes Assign a task to those processes.
'''



#example=1
from multiprocessing import Pool
def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)
'''
output:
1
4
9
16
25
'''
        
        
#example 2:
from multiprocessing import Pool
import time
def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x
    return sum
if __name__ == "__main__":
    t1=time.time()
    p = Pool()
    result = p.map(f,range(10000))
    p.close()
    p.join()
    print('pool took:',time.time()-t1)
    
'''
output:
pool took: 0.43114209175109863
'''
