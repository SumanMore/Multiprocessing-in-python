#sharing the data between the process using array and value\

Using array:
import multiprocessing

def calc_square(numbers, result):
    for idx, n in enumerate(numbers): #shared memory iteration is different idx is index n is the value
        result[idx] = n*n # put the value n*n in the idx index

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3) #result is shared memory variable( i is the data type that is integer and 3 is size of numbers list)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result)) #passing the shared memory variable i.e result 
    p.start()
    p.join()
    print(result[:])
'''output: [4,9,25]'''
    
    
    
    

import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers): #shared memory iteration is different idx is index n is the value
        result[idx] = n*n # put the value n*n in the idx index

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3) #result is shared memory variable( i is the data type that is integer and 3 is size of numbers list)
    v = multiprocessing.Value('d', 0.0) #d is the data type double and 0.0. is the value
    p = multiprocessing.Process(target=calc_square, args=(numbers, result, v)) #passing the shared memory variable i.e result 

    p.start()
    p.join()

    print(v.value)
'''output:5.67'''
