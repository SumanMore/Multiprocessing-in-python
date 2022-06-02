#instead of printing the result lets sytore it in a variable
'''when we create a new process what happens is it will create a create a new copy of square result global variable 
every process has their own address space so this process p1 will copy the global state and create its own address space so that the copy 
of square result is different and the result does not through  to original variable basically if we try to print the variable within the
process it will work'''
import multiprocessing
square_result=[]
def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square ' + str(n*n))
        square_result.append(n*n)
        print('within a process:result'+str(square_result))



if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()#process p1 starts executing#
    p1.join()
    print('result'+str(square_result))#it will give a empty list
    print("Done!")
    
'''
output:
square 4
within a process:result[4]
square 9
within a process:result[4, 9]
square 64
within a process:result[4, 9, 64]
result[]
Done!
'''
