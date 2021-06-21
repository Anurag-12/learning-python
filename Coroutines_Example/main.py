'''
 Both generator and coroutine operate over the data; the main differences are:
    Generators produce data
    Coroutines consume data

Coroutines are mostly used in cases of time-consuming programs, such as tasks related to machine learning or deep learning algorithms or in cases
 where the program has to read a file containing a large number of data. In such situations, we do not want the program to read the file or data, 
 again and again, so we use coroutines to make the program more efficient and faster. Coroutines run endlessly in a program because they use a while 
 loop with a true or 1 condition so it may run until infinite time. Even after yielding the value to the caller, it still awaits further instruction 
 or calls. We have to stop the execution of coroutine by calling coroutine.close() function.    
Syntax:
def myfunc():
    while True:
        value = (yield)


Execution is the same as of a generator. When you call a coroutine, nothing happens. They only run in response to the next() and send() methods. 
Coroutine requires the use of the next statement first so it may start its execution. Without a next() it will not start executing. We can search 
a coroutine by sending it the keywords as input using object name along with send(). The keywords to be searched are send inside the parenthesis. 
    send() — used to send data to coroutine
    close() — to close the coroutine
'''



def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on anurag and code with anurag and good"
    time.sleep(4)

    while True:
        text = (yield)  # whatever name is being passed to search  
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("anurag")

search.close()
#search.send("anurag")  # this will throw error since the coroutine is closed 



###############################################################

def names():

    import time

    names = "anurag harry haris carry amit ajey bhuvan shubham rahul aftab hrithik vivek ujjawal mohit rohit"

    time.sleep(2)

    while True:

        text = (yield)

        if text in names:

            print("Your name is in the list.")

        else:

            print("Your name is not in the list.")


name = names()
next(name)
name.send(input("Type your Name: "))

