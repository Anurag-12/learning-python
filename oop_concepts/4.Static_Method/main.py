'''
Static Method in Python:

We know that a static method in Python is treated differently than in other languages. Static methods in Python are extremely similar 
to python class methods, but the difference is that a static method is bound to a class rather than the objects for that class.
To define a static method, we use @staticmethod decorator, which is a built-in decorator. Also, there is no need to import any module 
to use decorators. Using a static method in a class, we permit it to be accessed only by the class objects or inside the class.

    There are few limitations related to static methods, such as:

    Unlike, class method a static method cannot alter or change any variable value or state of the class.
    Static methods do not have any knowledge related to class

Advantages of Python static method

Static methods have a very clear use-case. When we need some functionality not for an Object but with the complete class, we make a method static. This is advantageous when we need to create utility methods.
Finally, note that in a static method, we do not need the self or cls to be passed as the first argument.

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
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

Employee.printgood("Rohan")
