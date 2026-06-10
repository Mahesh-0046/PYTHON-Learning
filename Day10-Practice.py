#Arbitrary Arguments
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Keyword Argument
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Lamda Function
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Lists:
thelist = ["apple", "banana", "cherry"]
print(thelist)

#--->
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To know the length of the list len()
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

#To know the type of the list type()
mylist = ["apple", "banana", "cherry", "apple", "cherry"]
print(type(thislist))

#list constructor (create list another way like this)
mylist = list(("apple", "banana", "cherry", "apple", "cherry"))
print(mylist)

#Access list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#Range od negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Check if item exits
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
    print("apple is present in the list")
else:
    print("Not present in the list")

#Change item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrent"
print(thislist)

#change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrent", "watermelon"]
print(thislist)

#Example
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrent", "watermelon"]
print(thislist)

#Insert items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "blackcurrent")
print(thislist)

#Append items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove specified item
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

#Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

#Delete keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#loop through index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#Using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]