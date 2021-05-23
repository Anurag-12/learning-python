#Create a sample dictionary and take input from the user and return meaning and no error handling done !!

Dictionary = {"Mutable":"can change","Immutable":"can not chnage","Sly":"Cunning","Abscond":"run away, often taking something or somebody along"}
print(Dictionary.keys())
a = input("Enter any of the above words to know the meaning:")
b = a.capitalize()
print(b,"=",Dictionary[b])
