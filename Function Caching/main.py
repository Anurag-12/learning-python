'''
What is the term caching means?
Caching means to store the data in a place from where it can be served faster. In case of data that has been frequently used, the computer assigns a
 cache memory, so it does not have to load it again and again from the main memory. The purpose of the cache is to make the tasks more efficient and 
 quicker.

 How to use function caching in Python?
 We have been facilitated with the help of a decorator known as lru_cache.
 from functools import lru_cache 

 We have to pass maxsize as parameter with the decorator. maxsize is defined to tell the program how many values we want to store in the cache. 
 It automatically stores the values for the latest number of calls. 
'''


import time
from functools import lru_cache

@lru_cache(maxsize=32)  # it will store the value of last 32 calls 
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)  # here we have some logical function being executed which takes n sec
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)  # here it will not have to wait agin for 3 sec 
    print("Called again")

