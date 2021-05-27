#This code will change the current file position to 5, and print the rest of the line.
# Note: not all file objects are seekable.
f = open("myfile.txt", "r")
f.seek(5)
print( f.readline() )
f.close()


f = open("myfile.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
###################################################

#  With open(“file1txt”) as f, open(“file2.txt”) as g

'''advantages of With block:
    Multiple files can be opened.
    The files that are opened together can have different modes
    Automatically closes file
    Saves processing power by opening and closing file only when running code inside the block
'''

with open("harry.txt") as f:
    a = f.readlines()
    print(a)

# f = open("harry.txt", "rt")
# f.close()
  
