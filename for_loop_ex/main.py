items = [int, float, "Anurag", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)


######################33
list = [int, float, "Anurag", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for items in list:

    if type(items) == int and items>=6:

        print(items)