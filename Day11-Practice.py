#List comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
    print(newlist)

#With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#Iterable
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Expression
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

#Sort
fruits = ["mango", "banana", "cherry","apple", "kiwi", "kiwi"]
fruits.sort()
print(fruits)

#Sort numeric
numbers = [10, 9, 6, 20, 1]
numbers.sort()
print(numbers)

#Sort Descending
fruits = ["mango", "banana", "cherry","apple", "kiwi",]
fruits.sort(reverse = True)
print(fruits)

#Customize sort Function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#case insensitive sort
fruits = ["mango", "banana", "Cherry","apple", "Kiwi"]
fruits.sort()
print(fruits)

#lower case conversion before excution
fruits = ["mango", "banana", "Cherry","apple", "Kiwi"]
fruits.sort(key = str.lower)
print(fruits)

#Reverse order
fruits = ["mango", "banana", "cherry","apple", "kiwi"]
fruits.reverse()
print(fruits)

#Copy a list
thislist = [100, 50, 65, 82, 23]
mylist = thislist.copy()
print(mylist)

#Another method to copy list
thislist = ["mango", "banana", "cherry","apple", "kiwi"]
mylist = list(thislist)
print(mylist)

#Slice Operator (We can copy a list by using :(slice) operator)
thislist = ["mango", "banana", "cherry","apple", "kiwi"]
mylist = thislist[:]
print(mylist)

#Join two lists
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
list3 = list1 + list2
print(list3)

#Another way to join two lists
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
for i in list2:
    list1.append(i)
print(list1)

#Extend() method to join lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)
print(list1)

#Tuple
tuple1 = ("abc", 12, True, 42, "male")
print(type(tuple1))
print(tuple1)

#The Tuple construtor
thistuple = (("apple", "banana", "cherry")) #note double brackets
print(thistuple)

#Index
thistuple = ("apple", "banana", "cherry")
print(thistuple[2])

#Check ifitem exits
thistuple = ("apple", "banana", "cherry")
if "banana" in thistuple:
    print("Yes, 'banana' is in the thistuple")
else:
    print("Not Exist")

#Change tuple values(convert to list then change values and again change it to tuple)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add a tuple to another tuple
x = ("apple", "banana", "cherry")
y = ("orange",)
x += y
print(x)

#Remove item
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)

'''Delete tuple
x = ("apple", "banana", "cherry")
del x
print(x) #Throws an error after del nothing will be there to execute'''

#Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#Using Asterisk*
fruits = ("apple", "banana", "cherry", "pineapple", "mango")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Loop through tuple
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#While loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

#Join two tuples
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c", "d")
tuple3 = tuple1 + tuple2 
print(tuple3)

#Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)