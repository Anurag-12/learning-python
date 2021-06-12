'''
“An abstract class is a class that holds an abstract method.”
And
“An abstract method is a method defined inside an abstract class.”

The definition may appear too simple, but the abstract method holds all the cards because it is necessary for all classes that are 
being derived by the abstract class to have the same method even though their functionality and code msy differ. However, the name 
of method should be the same as the abstract method. The abstract method inside the abstract class could even be empty because we 
can not implement it anywhere. It is just so that all the other classes define a method by the same name. 

It is important to remember that, we can not make an object for abstract class.
 syntax: 

from abc import ABC, abstractmethod
Class MyClass(ABC):
      @abstractmethod
      def mymethod(self):
            #empty body
            pass

We have to pass ABC to the class we are defining as abstract. To make a method specifically abstract in a class, we use the abstract
method decorator denoted as @absttractmethod, which is defined in the abc module.

Important points about abstract class in Python:

    Abstract methods are defined in the abstract class. Mostly they do not have the body, but it is possible to have abstract methods with implementation in the abstract class. Any subclass deriving from such abstract class still needs to provide an implementation for that abstract methods.
    An abstract class can have both abstract methods as well as concrete methods.
    The abstract class works as a template for other classes. 
    By using the abstract class, we can define a structure without providing a proper implementation of every method. 
    It is not possible to create objects of an abstract class because Abstract class cannot be instantiated.
    An error will occur if the abstract method has not been implemented in the derived class.

'''

# Sample Example 
# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())


#It is not possible to create objects of an abstract class because Abstract class cannot be instantiated.

# rect2 = Shape()   # will throw error "Can't instantiate abstract class Shape with abstract method"

