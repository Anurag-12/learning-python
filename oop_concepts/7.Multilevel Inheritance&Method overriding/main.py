'''
What is Multilevel Inheritance in Python?
In multilevel inheritance, a class that is already derived from another class is derived by a third class. 
So in this way, the third class has all the other two former classes' features and functionalities. 
The syntax looks something like this:
    class Parent1:
    pass
    class Derived1(Parent1):
    pass
    class Derived2(Derived1):
    pass

Now let us dive into the priority brought by the ordering of the class. Suppose that we are looking for a constructor or a value 
for any variable. Our program will first check our current class i.e., Derived2, for it. If nothing found, then it will move towards 
Derived1 and in order at last towards Parent1 until it finds the constructor or variable in the way.
If we have the same method or variable in the base and derived class, then the order we discussed above will be followed, 
and the method will be overridden.

Rules for Method overriding:-
    The name of the child method should be the same as parents.
    Inheritance should be there, and we need to derive a child class from a parent class
    Both of their parameters should be the same.

'''

class Dad:
    basketball =6

class Son(Dad):
    dance =1
    basketball = 9 # overriding
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6 # overriding
    guitar = 1

    def isdance(self): # overriding
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.basketball)

