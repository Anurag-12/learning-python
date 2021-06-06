'''
As we have observed in the previous tutorials, we cannot change the value of a variable defined in the class from outside, 
using an object. Instead, if we try that, a new instance variable will be created for the class having the value we assigned. 
But no change will occur in the original value of the variable.
We saw the use of self keyword in the previous tutorial. In this tutorial, we are going to know the working of a 
new keyword i.e., cls. Class methods take cls parameter that points to the class and not the object instance when the method is called.

Syntax:
class myClass:
    @classmethod
    def myfunc (cls, arg1, arg2, ...):

A quick overview:

Python class method is a way to define a function for the Python class. 
It receives the class as an implicit first argument. Using @classmethod decorator, it is possible to create as many constructors 
for a class that behaves like a factory constructor. 
'''



class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))           # in on line of code using concept of *args 


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.no_of_leaves)
# rohan.change_leaves(34)
#
# print(harry.no_of_leaves)

