'''
What is OS Module?
OS module provides our code with a direct connection to the operating system. We can use its different functions to interact and do activities on 
our operating system. For example, if we want to create such software that needs to store or access files from a directory or folder, we can use the
 OS module to perform the task for us. To use OS Module in Python, we have to import it.

 The main purpose of the OS module is to interact with the operating system. The primary use of the OS module is to create folders, remove folders, 
 move folders, and sometimes change the working directory. OS module has a lot of built-in functions,You can explore more OS module build-in function
  by reading its python documentation.
'''



import os
# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
print(os.path.isfile("C://Program Files"))
