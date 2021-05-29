'''
First argument is always normal argument, second position is args(datatype of args is tuple but takes list and tuple both ) 
and third argument is kwargs(dictionary)

Note: “We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts
 about the number of  arguments we should pass in a function.” 
'''

def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)
  
