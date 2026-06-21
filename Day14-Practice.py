#File Handling
#Open a File on the Server
f = open("demofile.txt")
print(f.read())

#Using the with statement
with open("demofile.txt") as f:
    print(f.read())

#To close file
f = open("demofile.txt")
print(f.read())
f.close()

#Read only parts of the file
with open("demofile.txt") as f:
    print(f.read(5))

#Read line
with open("demofile.txt") as f:
    print(f.readline())

#Another example to read all lines one by one
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())

#loop through readline()
with open("demofile.txt") as f:
    for x in f:
        print(x)

#Write to an Existing file
with open("demofile.txt", "a") as f:
    f.write( "Now the file has more content!")

#Overwriting Existing Content
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content")

'''#Create a New file
f = open("myfile.txt", "x")

#Delete a File
import os
os.remove("myfile.txt")'''

#Check file if exist
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

#Working with Different files
#Reading CSV file
with open("data.csv", "r") as f:
    for line in f:
        print(line.strip().split(","))

#Writing to CSV file
rows = [
    ["Name", "Score"],
    ["Alice", 85],
    ["Bob", 90]
]
with open("data.csv", "w") as f:
    for row in rows:
        f.write(",".join(map(str, row)) + "\n")

#Python Error Handling
#Error Handling with files
try:
    print(x)
except:
    print("An exception occurred")

#Many Exceptions
try:
    a = 10 / 0
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#Else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#Finally
try:
    print(x)
except:
    print("Something else went wrong")
finally:
    print("the 'try except' is finished")

#Raise an Exception
x = -1
if x < 0:
    raise TypeError("Sorry, no numbers below zero")

#Another example
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

#Handling Specific Exceptions
try:
    num = int(input("Enter a number:"))
    result = 10 / num
except ValueError:
    print("Please enter a valid integer")
except ZeroDivisionError:
    print("You cannot divide with zero")

#Getting Exception Details
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Exception type: {type(e).__name__}")
    print(f"Message: {e}")

#Raising Exceptions Manually
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    balance -= amount
    return balance

try:
    print(withdraw(100, 150))
except ValueError as e:
    print(f"Transaction failed: {e}")

#Custom Exception Classes
class InsufficientBalanceError(Exception):
    """Custom exception for low balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance: {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    balance -= amount
    return balance

try:
    withdraw(100, 200)
except InsufficientBalanceError as e:
    print(e)

#Raising Exceptions with Cause
try:
    x = int("abc")
except ValueError as e:
    raise RuntimeError("Failed to convert input") from e

#Nested try/except Blocks
try:
    with open("data.txt", "r") as f:
        try:
            val = int(f.readline())
        except ValueError:
            print("File contains invalid number.")
except FileNotFoundError:
    print("File missing.")