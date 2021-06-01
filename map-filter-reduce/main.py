'''
map():
"A map function executes certain instructions or functionality provided to it on every item of an iterable."
The iterable could be a list, tuple, set, etc. It is worth noting that the output in the case of the map is also an iterable i.e., a list. 

Syntax: map(function, iterable) 
'''
#Example :
items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x **3), items))
print(a)
#Output: [1, 8, 27, 64, 125]

'''
filter():-

"A filter function in Python tests a specific user-defined condition for a function and returns an iterable for the elements and values that 
satisfy the condition or, in other words, return true."

Syntax: filter(function, iterable)
'''
#Example :
a = [1,2,3,4,5,6]
b = [2,5,0,7,3]
c= list(filter(lambda x: x in a, b))
print(c) 
# prints out [2, 5, 3]


'''
reduce():

"Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant".
We have to import reduce from functools

Syntax :  reduce(function, iterable)
'''
# Example 
from functools import reduce
a=reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
print(a) 
#Output: 24



#--------------------------MAP------------------------------
# numbers = ["3", "34", "64"]
# numbers = list(map(int, numbers))  #to type cast to int 

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])

# numbers[2] = numbers[2] + 1
# print(numbers[2])
#----
# def sq(a):
#     return a*a
#
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq, num))
# print(square)
# num = [2,3,5,6,76,3,3,2]
# square = list(map(lambda x: x*x, num))
# print(square)

#---
# def square(a):
#     return a*a
#
# def cube(a):
#     return a*a*a

# func = [square, cube]
# for i in range(5):
#     val = list(map(lambda x:x(i), func)) # will give square and cube of the number from 1-5 . eg : [4,8] for 2 
#     print(val)

#--------------------------FILTER------------------------------
# list_1 = [1,2,3,4,5,6,7,8,9]
#
# def is_greater_5(num):
#     return num>5
#
# gr_than_5 = list(filter(is_greater_5, list_1))  # will give number greater than 5 from list_1 
# print(gr_than_5)
#--------------------------REDUCE------------------------------
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x+y, list1)   #will give the sum of all the number in the list1 
# num = 0
# for i in list1:
#     num = num + i
print(num)










