'''
Method:
A method is just like a function, with a def keyword and a single parameter in which the name of the object has to be passed. 
The purpose of the method is to show all the details related to the object in a single go. 
We choose variables that we want the method to take but do not have to pass all of them as parameters. 
Instead, we have to set the parameters we want to include in the method during its creation. 
Using methods make the process simpler and a lot faster. 

Self keyword:
The self keyword is used in the method to refer to the instance of the current class we are using. 
The self keyword is passed as a parameter explicitly every time we define a method.

__init__ method:-
"__init__" is also called as a constructor in object-oriented terminology. Whereas a constructor is defined as:

"Constructor in Python is used to assign values to the variables or data members of a class when an object is created."
As there can be only one constructor for a specific class, so the name of the constructor is a constant, i.e., __init__.

Types of constructors in Python
    We have two types of constructors in Python.

    1. The default constructor is the one that does not take any arguments.
    2. Constructor with parameters is known as parameterized constructor.

'''

# SAMPLE EXAMPLE 

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"  # To avoid passing individual object variable we have created __init__ construtor above 
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)
print(harry.printdetails())

