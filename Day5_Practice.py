#Create variables for your own name, age, and height in meters.
name = "Mahesh"
age = 28
height = 1.66

#Convert height from float to string and print a sentence with it using print().

height = str(height)
print("My name is "+ name, "and my height is "+ height, "meters")

#Ask the user for their name and then display.
name = input("Enter your name: ")
print("Welcome " + name)

#Take temperature in Celsius as input and print the equivalent in Fahrenheit.
#Formula: F = C * 9/5 + 32.
Celsius = float(input("Enter Temperature in Celsius: "))

Fahrenheit = (Celsius * 9/5) + 32

print("Temperature in Fahrenheit: ", Fahrenheit)

#Prompt the user for two numbers and an operation (+, -, *, /).

Num1 = float(input("Enter First Number: "))
Num2 = float(input("Enter Second Number: "))

Operation = input("Enter an Operatio (+, -, *, /): ")

if Operation == '+':
    print("Result: ", Num1 + Num2)

elif Operation == '-':
    print("Result: ", Num1 - Num2)

elif Operation == '*':
    print("Result: ", Num1 * Num2)

elif Operation == '/':
    if Num2 == 0:
        print("Cannot Divide by Zero")
    else:
        print("Result: ", Num1 / Num2)

else:
    print("Invalid Operation")


#Arithmatic Operators:
a = 10
b = 3
print("a + b: ", a + b)  #Addition
print("a - b: ", a - b)  #Subtraction
print("a * b: ", a * b)  #Multiplication
print("a / b: ", a / b)  #Division (float)
print("a // b: ", a // b)  #Floor Division
print("a % b: ", a % b)  #Modulus
print("a ** b: ", a ** b)  #Exponent

#Relational Operators:
a = 10
b = 3
print("a == b: ", a == b)  #Equal to
print("a != b: ", a != b)  #Not equal to
print("a > b: ", a > b)  #Greater than
print("a < b: ", a < b)  #Less than
print("a >= b: ", a >= b)  #Greater than or equal to
print("a <= b: ", a <= b)  #Less than or Equal to

#Logical Operators:
x = True
y = False
print("x and y:", x and y)  #AND
print("x or y:", x or y)  #OR
print("not x:", not x)  #NOT

#Assignment Operators
c = 5
print("Initial c =", c)
c += 2
print("c after c += 2 :", c)
c -= 1
print("c after c -= 1 :", c)
c *= 3
print("c after c *= 3 :", c)
c //= 2
print("c after c //= 2:", c)
c %= 4
print("c after c %= 4 :", c)
c **= 2
print("c after c **= 2:", c)

#Bitwise Operators
m = 5  #binary: 0101
n= 3  #binary: 0011
print("m & n =", m & n)  #AND
print("m | n =", m | n)  #OR
print("m ^ n =", m ^ n)  #XOR
print("~m =", ~m)   #NOT(invert bits)
print("m << n =", m << 1)  #Left shift
print("m >> n =", m >> 1)  #Right shift

#Membership Operators
nums = [1, 2, 3, 4]
print("2 in nums :", 2 in nums)  #True
print("7 not in nums :", 7 not in nums)  #True

#Identity Operator
p = [1, 2, 3]
q = p
r = [1, 2, 3]
print("p is q  :", p is q)   #True (same object)
print("p is r  :", p is r)   #False (different object)
print("p is not r  :", p is not r)   #True