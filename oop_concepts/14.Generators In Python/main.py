
# def Factorial_gen(n):

#     fac = 1

#     for i in range(n):

#         fac = fac * (i + 1)

#         yield fac

#     # return fac

# number = int(input("Enter the number:"))

# c= Factorial_gen(number)

# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())



# d= int(input('Give amount: '))

# def fib(n):

#     a, b = 0, 1

#     for _ in range(n):

#         yield a

#         a, b = b, a + b

# print(tuple(fib(d)))

def fibo(limit):

     a, b = 0, 1



     while a < limit:

          yield a

          a, b = b, a+b



for i in fibo(10):

    print(i)