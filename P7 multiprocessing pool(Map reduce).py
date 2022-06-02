from multiprocessing import Pool
def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)
        
        
        
        
example 2:
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
    
