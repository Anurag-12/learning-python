'''
SON stands for JavaScript Object Notation. JSON is a data-interchange format, derived from JavaScript. It is mostly used for storing or 
transferring data. So, if we want our program to interact with the internet, we must be familiar with this module, even only to send or
 receive data through the internet.
  A JSON is an unordered collection of key and value pairs similar to a python dictionary. The following are some important points about JSON.
  
    Keys are unique strings that cannot be null.
    Values can be anything from a String, Number, Tuple, Boolean, list, or null.
    A JSON is represented by a string which is enclosed within curly braces { } with key-value pairs which are separated by a colon ( : ), 
    and pairs separated by a comma(, ).


If we convert a JSON string to a Python, the resultant will be a dictionary. The conversion is also known as parsing, and that is the 
keyword we use professionally for the conversion. We can either convert from JSON to Python or from Python to JSON by using json.loads() 
or json.dumps() methods. Methods:

    load(): This method is used to load data from a JSON file into a python dictionary.
    Loads(): This method is used to load data from a JSON variable into a python dictionary.
    dump():This method is used to load data from the python dictionary to the JSON file.
    dumps(): This method is used to load data from the python dictionary to the JSON variable.

import json
a ={"name":"harry","salary":9000,"language":"Python"}  
# conversion to JSON done by dumps() function
b = json.dumps(a)
print(b) # printing the output

output : {"name": "harry", "salary": 9000, "language": "Python"}

What parsing actually does?
Parsing converts the code from one form to another, making it compatible with running on the other platform by changing all the little 
syntax differences and making it perfect for running on the other platform. The following table shows how Python objects are converted 
to JSON objects.
JSON 	    PYTHON
true      	true
false    	false
string      string
number  	number
array     	list, tuple
object  	dict
null       	none
'''

import json

data = '{"var1":"anurag", "var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))
print(parsed['var1'])


data2 = {
    "name": "anurag",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps
sort_keys :If sort_keys is true (default: False), then the output of dictionaries will be sorted by key. 
