#Practice
'''Ask the user to enter a password:
●	If length < 6 → “Too short”
●	If contains spaces → “No spaces allowed”
●	Else → “Password accepted”
Bonus: Use logical operators to combine the checks into fewer lines.'''

user = input("Enter a password: ")

if len(user) < 6:
    print("Too short")
elif " " in user:
    print("No spaces allowed")
else:
    print("Password allowed")

#or
user = input("Enter a password: ")

if len(user) >= 6 and " " not in user:
    print("Password allowed")
else:
    print("Password Not allowed")

#Match Statement
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Only 7 day in a week")

#Another Example
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends")

#Example
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in april")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
#-----------------------------------------------------------------------------------------

#Loops(The while loop)
#Break Example
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Continue Example
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#For loop
fruits = ["banana", "apple", "cherry"]
for x in fruits:
    print(x)

#break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Another Example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
       break
   print(x)

#Continue statement for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
       continue
   print(x)

#Range
for x in range(2, 30, 3):
    print(x)

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

#The pass statement
for x in [0, 1, 2]:
    pass