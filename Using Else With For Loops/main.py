'''How we can implement for-else in Python?
We have to write an else statement using the Else keyword, followed by a colon after the ending of the for loop block of code.
Syntax:
for x in n: 
   #statements
 else:
   #statements

When we use else with for loop the compiler will only go into the else block of code when two conditions are satisfied:
    
    The loop normally executed without any error.
    We are trying to find an item that is not present inside the list or data structure on which we are implementing our loop.

Except for these conditions, the program will ignore the else part of the program. For example, if we are just partially executing 
the loop using a break statement, then the else part will not execute. So, a break statement is a must if we do not want our compiler
to execute the else part of the code.
'''
# Example :1
for i in ['C','O','D','E']:
    print(i)
else: 
    print("Statement successfully executed")


#Example : 2 

khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "rotiroll":    # if true than else will not be executed i.e. if item == "roti"  than else will not be executed 
        break

else:
    print("Your item was not found")


'''
Why we implement the else functionality with for loops?
We mostly use such implementations in our program when we want to encounter less logical errors and want to know that our program is functioning correctly. 
In such cases, we will most probably send a print statement inside the code, and based on its execution, we could see if our code is working correctly. 
'''
    


