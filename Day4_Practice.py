#Reassigning variables.
x = 4
x = "Sally"
print(x)

#String variables can be declared either by using single or double quotes:
x = "john"
# is the same as
x = 'john'

#Variable names are case-sensitive.
a = "Sally"
A = "Salt"
print(a, A)
#A will not overwrite a

#Function Example:
x = "Awesome"

def myfunc():
    x = "Fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

#Check Example with comparison
x = "Awesome"

def myfunc():
    global x
    x = "Fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

#Type Conversion:
# int("42"), str(3.14), float("5.5"), bool(0).
y = int(2.8)
x = float(1)
y = str(2)    
z = str(3.0)

#User Input
name = input("Enter your name: ")
print("Hello", name)
