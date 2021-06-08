'''
Access modifiers are used for the restrictions of access any other class has on the particular class and its variables and methods. 
In other words, access modifiers decide whether other classes can use the variables or functions of a specific class or not. 

In Python, there are three types of access modifiers.
    Public Access Modifier
    Protected Access Modifier
    Private Access Modifier
'''

# Public Access Modifier: 
# In public, all the functions, variables, methods can be used publicly. 
# Meaning, every other class can access them easily without any restriction. 
# Public members are generally methods declared in a class that is accessible from outside the class. 
# Any ordinary class is by default, a public class.

# Exampole 
class employee:
      def __init__(self, name, age):
            self.name=name
            self.age=age

# Protected Access Modifier:
# In case of a protected class, its members and functions can only be accessed by the classes derived from it, i.e. its child class 
# or classes. No other environment is permitted to access it. To declare a class as protected, we use a single underscore “_” sign 
# before the data members of the class. 

# Example 
class employee:
      def __init__(self, name, age):
            self._name=name # protected attribute 
            self._age=age # protected attribute


# Private Access Modifier:
# In the case of private access modifiers, the variables and functions can only be accessed within the class. 
# The private restriction level is the highest for any class. To declare a class as private, we use a double underscore “_­_” sign 
# before the data members of the class. Here is a suggestion not to try to access private variables from outside the class, because 
# it will result in an AttributeError. 

# Example 
class employee:
      def __init__(self, name, age):
            self.__name=name # private attribute 
            self.__age=age # private attribute


'''
Name mangling in Python:
Python does not have any strict rules when it comes to public, protected or private, like java. So, to protect us from using the private attribute in any other class, 
Python does name mangling, which means that every member with a double underscore will be changed to _object._class__variable when trying to call using an object. 
The purpose of this is to warn a user, so he does not use any private class variable or function by mistake without realizing its states.

The use of single underscore and double underscore is just a way of name mangling because Python does not take the public, private and protected terms much seriously so
 we have to use our naming conventions by putting single or double underscore to let the fellow programmers know which class they can access or which they can't.
'''


class Employee:
    no_of_leaves = 8 # public 
    var = 8  # public 
    _protec = 9   # protected
    __pr = 98  # private 

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

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)  # Name mangling 
print(emp.var) 
print(emp._protec) 
