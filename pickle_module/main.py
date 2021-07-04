'''
What is pickling?
Pickling is a process of serializing an object. Serializing means to store the object in the form of binary representation so it can be
saved in our main memory. The object could be of any type. It could be a string, tuple, or any other sort of object that Python supports.
The data is stored in the main memory in a file. While writing the code for pickling, we open the file in "wb" mode, also known as writing 
binary mode. So, to use the pickle module, we have to make a file with .pkl extension and send it in a dump() function along with the object.
dump() is a built-in function in the Pickle module, made for pickling.

What is unpickling?
The file format is binary, so we cannot directly open and read it; instead, we have to open it using a python program, and the process is
 known as unpickling. For unpickling, we have to open the file in "rb" mode, also known as a read binary mode. The function we use this time 
 is also a built-in function, named load(). Unlike dump(), we have to send the file name as a parameter, and it automatically retrieves the 
 data in the object type it was inserted in. For example, if we send a list while pickling, the return result will also be a list.

We can face some of the common pickle exceptions raised while dealing with pickle module.

    Pickle.PicklingError: If the pickle object does not support pickling, then Pickle.PicklingError exception is raised.
    Pickle.UnpicklingError: This exception will raise if the file contains bad or corrupted data.
    EOF Error: This exception will raise if the end of the file is detected.

Disadvantages:

    There are some situations in which pickling is discouraged. For example, when we are working with multiple programming languages, pickle is discouraged.
    Pickle has been found slower than its alternatives.
    In some cases, it has also shown a few security vulnerabilities.
    When we update our program to a newer version, pickled data through the previous version can cause issues.

'''
# pickle.loads() = This function takes a byte string as argument.
# pickle.load() = This function takes a  file-like object as argument.
# # This was the same analogy you can take from json.load() and json.loads()


import pickle

#Pickling a python object

# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')    # wb write binary 
# pickle.dump(cars, fileobj)
# fileobj.close()


#Un-Pickling a python object

file = "mycar.pkl"
fileobj = open(file, 'rb')  # rb read binary 
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))







