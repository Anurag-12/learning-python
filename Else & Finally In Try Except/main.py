'''
try and except block:

In the try block, we write the code in which an exception might occur, and in except block, we write the code as a resultant if an exception occurs. 
This could either be a print statement or the error itself. If no exception occurs, the except block will not execute. The purpose of try and except 
is to keep the program running either an error or exception occurs. 

else keyword:-
Now moving onto the else keyword. We use an else keyword to print something in cases where no exception occurs. Suppose that an exception occurred, 
and the except block is printing the error, likewise if the exception does not occur, we can print a statement that no error occurred, using an else 
keyword. Syntax of using else with try and except block is:

def divide(a, b):
    try:
        print(f'{a}/{b} is {a / b}')
    except ZeroDivisionError as e:
        print(e)
    else:
        print("No Exception")
divide(1, 2)

# output : 
 1/2 is 0.5
No Exception

# Note: An else will only run in case where no exception occurs.


finally:-
 finally, will run in either case. It is also known as code cleaner because it will perform its action, either an exception occurs or not. 
 We write such commands in the finally part of code that we want to execute even an exception occurs or not. It is mostly used to clean resources or
close files. 

try:
    #Run this code
except Exception as error:
    #Execute this code when there is an exception
else:
   #No Exception. Run this code
finally:
   #Always run this code
'''
'''
Summing Up

    In the try block, all the statements are executed until an exception occurs.
    Except block is used to catch and handle the exception(s) that occurs during the execution of the try block.
    Else block runs only when no exceptions occur in the execution of the try block.
    Finally block always runs, either an exception occurs or not.

'''

f1 = open("anurag.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")

