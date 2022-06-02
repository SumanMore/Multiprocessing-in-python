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
