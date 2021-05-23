items = [int, float, "Anurag", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)


######################33
list = [int, float, "Anurag", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for items in list:

    if type(items) == int and items>=6:

        print(items)
        
        
######
#while loop sample 
# Continuously takes input from user untill its greater than 100

while(True):
    inp = int(input("Enter a Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try again!\n")
        continue
