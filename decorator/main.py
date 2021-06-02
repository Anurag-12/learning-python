'''
Python Decorator
    Decorator as can be noticed by the name is like a designer that helps to modify a function. 
    The decorator can be said as a modification to the external layer of function, as it does not 
    make any change in its structure. What a decorator does is, it takes a function and insert some 
    new functionality in it without changing the function itself. A reference to a function is passed 
    to a decorator and the decorator returns a modified function. The modified functions usually contain 
    calls to the original function. This is also known as metaprogramming because a part of the program tries 
    to modify and add functionality into another part of the program at compile time.

    A wrapper is a function that provides a wrap-around another function. While using decorator all the code
    which are executed before our function that we passed as a parameter and also the code after it is executed
    belongs to the wrapper function. The purpose of the wrapper function is to assist us. Like if we are dealing
    with a number of similar statements, the wrapper can provide us with some code that all the functions have 
    in common and we can use a decorator to call our function along with wrapper. A function can be decorated many times. 

    There are two ways to write a Python decorator:
        We can pass our function to the decorator as an argument, thus define a function and pass it to our decorator.
        We can simply use the @ symbol before the function we'd like to decorate.
'''
# Note that a decorator is called before defining a function.

# Sample Function call eg
# def funcret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
#
# a = funcret(1)
# print(a)

def inner1(func): 
    def inner2():
        print("Before function execution"); 
        func() 
        print("After function execution")    
    return inner2 

#@inner1  #method1
def function_to_be_used(): 
    print("This is inside the function") 

#function_to_be_used = inner1(function_to_be_used) #method 2
function_to_be_used()  



'''
Advantages:

• Decorator function can make our work compact because we can pass all the functions to a decorator that requires the same sort 
  of code that the wrapper provides.
• We can get our work done, without any alteration in the original code of our function.
• We can apply multiple decorators to a single function.
• We can use decorators in authorization in Python frameworks such as Flask and Django, Logging and measuring execution time.

'''