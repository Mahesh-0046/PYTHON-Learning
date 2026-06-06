#Practice:
#Create a multiline string of your own (e.g., a short poem) and print it.
a = """Every day I learn a bit,
One small step, I won't quit.
Lines of code and bugs to fight,
Turning confusion into light."""
print(a)

#Practice: Take the string "DataScience" and print the first 4 letters, print the last 3 letters, reverse it.
A = "DataScience"
print(A[:4])
print(A[-3:])
print(A[::-1])

#Take a user input string, remove leading/trailing spaces and convert to lowercase. Count how many times the letter a appears.
txt = input("Enter a string: ")
print(txt.strip())
print(txt.lower())
print(txt.count("a"))

#Write a program that asks the user for a sentence and print it in reverse. 
#Also counts how many vowels (a, e, i, o, u) it contains and prints it in the title case (.title()).
text = input("Write a Sentence: ")
vowels = 0

for i in text.lower():
    if i in "aeiou":
        vowels += 1
print(text[::-1])
print("Number of vowels: ", vowels)
print("Title case: ", text.title())

#If statement
a = 33
b = 200
if b > a:
    print("b is grater than a")

#Elif statement
a = 33
b = 33
if b > a:
    print("b is grater than a")
elif b == a:
    print("b and a are equal")

#Else
a = 200
b = 33
if b > a:
    print("b is grater than a")
elif b == a:
    print("b and a are equal")
else:
    print("a is greater than b")

#Short hand if
a = 2000
b = 330
if a > b: print("a is greater than b")

#Short Hand If Else
a = 2
b = 330
print("A") if a > b else print("B")

#Nested If
x = 41
if x > 10:
    print("Above ten!")
    if x >20:
        print("and alse Above 20!")
    else:
        print("not above 20!") 

#Chained Comparisions
x = 8
if 0 < x < 10:
    print("x is between 1 and 9")

#in used in if statement
fruit = "akiwi"
if fruit in ["apple", "banana", "Mango"]:
    print("Fruit is available")
else:
    print("not available")

#The pass statement
a = 33
b = 200

if b > a:
    pass

"""Guided Exercise
1. Write a program that:
1.	Ask the user for their age.
2.	Prints:
○	“Child” if < 13
○	“Teenager” if 13–19
○	“Adult” if 20–64
○	“Senior” if 65+"""
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 64:
    print("Adult")
else:
    print("Senior")

#2. Check if a year is a leap year.
#(Hint: divisible by 4, but centuries must also be divisible by 400.)
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a Leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a Leap year")

#3. Take a string and print whether it is a palindrome (same forward/backward).
user = input("Enter a string: ")
if user == user[::-1]:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")