'''#Practice
#Print a multiplication table (1–10) using nested for loops.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} =", i * j)

#Ask the user for numbers until they type "stop"; then display the average.
total = 0
count = 0
while True:
    user = input("Enter a number (or) stop: ")
    if user == "stop":
        break

    total += float(user)
    count += 1

if count > 0:
    print("Average: ", total/count)
else:
    print("No numbers entered")

#Using a for loop and if, print only the vowels from a string.
user = input("Enter a string: ")

for i in user.lower():
    if i in "aeiou":
        print(i)'''


#Creating Function
def my_function():
    print("Hello, World")

my_function()

#Function with Arguments
def my_func(fname):
    print(fname + " Refdnes")

my_func("Emil")
my_func("Tobias")
my_func("Linus")

#Parameters and arguments should be match

#Default parameter value
def my_func(country = "Norway"):
    print("I am from "+ country)

my_func("India")
my_func()
my_func("Australia")

#Passing a list as an argument
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return value
def my_func(x):
    return 5 * x
print(my_func(3))
print(my_func(5))
print(my_func(9))

#Pass statement
def my_func(x):
    pass

#Nested Function
def outer():
    def inner():
        print("inner function")
    inner()
outer()

#Recursion
def try_recursion(k):
    if(k > 0):
        result = k + try_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results")
try_recursion(6)


#1.	Temperature Converter:
# Create a function c_to_f(celsius) that converts Celsius to Fahrenheit.
def c_to_f(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Enter temperature in Celsius: "))
print(f"{temp}°C = {c_to_f(temp)}°F")

#2.	List Stats:
# Write a function that takes a list of numbers and returns the minimum, maximum, and average.
def list_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average

nums = [10, 20, 30, 40, 50]

minimum, maximum, average = list_stats(nums)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)