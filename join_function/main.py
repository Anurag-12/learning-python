# syntax : string.join(iterable)

#join() with lists
numList = ['1', '2', '3', '4']
separator = ' , '
print(separator.join(numList))
# Output : 1, 2, 3, 4

#join() with lists Dictionary
# Drawaback : the join function will only return the key part, separated by the string in between, leaving the value side behind.
myDictionary = {"name": "Jack", "country": "America"}
separator = "_separator_"
print(separator.join(myDictionary))

#output :  name_separator_country

'''
In situations where the iterable consists of a multi-data type, such as a list or tuple consisting of all integer variables and one single, 
double variable, the join function will not work. Instead, it will display an error. 
For join to function properly, all the variables should have the same sort of data type, either it is an integer, string, or any other.
'''
inputlist = ["Test1",13,"Test2",24,"Test3",100,"Test4"]
sep = '_'
out = sep.join(inputlist)
print(out)

# OUTPUT : Traceback (most recent call last): File "./prog.py", line 3, in TypeError: sequence item 1: expected str instance, int found


lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = " and ".join(lis)
print(a, "other wwe superstars")

#output: John and cena and Randy and orton and Sheamus and khali and jinder mahal other wwe superstars
