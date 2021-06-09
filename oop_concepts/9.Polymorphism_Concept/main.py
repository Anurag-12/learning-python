'''
What Is Polymorphism?

In basic English language, Polymorphism means to exist in different states. The same object or thing changing its state from one
form to another is known as polymorphic. A same function or method, being used differently in different scenarios can perfectly 
describe polymorphism. It occurs mostly with base and derived class.  

Understanding Polymorphism in Python
The concept of polymorphism has very strong ties with method overriding concept  along with super() function
For example, if a method in the child class that has the same name as the methods in the parent class and also they take the 
same number of variables as parameters, then the child class will inherit the methods from the parent class and will override 
the method too. Meaning that the compiler will execute the method in the child because it will be the first place it looks while 
searching for the method when called. By overriding a method, we can also add some more functionalities in it, so in a way modifying 
the method in the child class but letting it remain the same in the parent class.
'''
#Example
len("Python") # returns 6 as result
len([1,2,3,4,5,6,7,8,9]) # returns 9 as result
'''
Python also implements polymorphism using methods. The len() method returns the length of an object. In this case, the function len()
is polymorphic as it is taking a string as input in the first case which returns total length/characters of the string and in the
second case, it is taking list as input.
 Polymorphism is a very important concept. Although being a theoretical concept, it is of great importance as it teaches us to use one 
 entity,let it be a method or variable, differently at different places.
'''

#Polymorphism in '+' operator:-


print(5+6) # output : 11
print("5" + "6")  #output : 56

def inner1(func): 
    def inner2():
        print("Before function execution"); 
        func() 
        print("After function execution")    
    return inner2 

@inner1  #method1
def function_to_be_used(): 
    print("This is inside the function") 

#function_to_be_used = inner1(function_to_be_used) #method 2
function_to_be_used()  
