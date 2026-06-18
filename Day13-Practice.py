#Dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict)

#We can find each key value also like this
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(thisdict["brand"])

#Duplicate not allowed
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}
print(thisdict)

#Dictionary length
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020
}
print(thisdict)
print(len(thisdict))

#Dictionary items
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964,
    "colors" : ["red", "white", "blue"]
}
print(thisdict)

#Type()
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964
}
print(type(thisdict))

#The dict() Constructor
thisdict = dict(name = "John", age = 30, city ="Hyderabad")
print(thisdict)

#Accessing items
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964
}
x = thisdict["brand"]
print(x)
#get() method same result x = thisdict.get("brand")

#Get keys
thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964
}
x = thisdict.keys()
print(x)

#Another example added a color key
car = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get values
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Get items
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Check if key exists
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
if "model" in car:
    print("Yes, 'model' key is there in car dictionary")
else:
    print("NO, it's not there in the car dictionary")

#Change values
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(car) #before the change
car["model"] = "Sedan"
print(car) #after the change

#Update dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.update({"year" : 2020})
print(thisdict)

#adding items
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)

#Remove items
#pop()
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.pop("model")
print(thisdict)

#popitem() this will remove last inserted key
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.popitem()
print(thisdict)

#del
"""thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del thisdict
print(thisdict)

#clear
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict.clear()
print(thisdict)"""

#Loop through a dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for i in thisdict:
    print(thisdict[i])

#values()
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for i in thisdict.values():
    print(i)

#keys()
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for i in thisdict.keys():
    print(i)

#to get keys and values
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
for i, j in thisdict.items():
    print(i, j)

#Copy a Dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
mydict = thisdict.copy()
print(mydict)

#We can copy by using built function dict() also
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested dictionary
myfamily = {
    "child1" : {
        "name" : "Rio",
        "year" : 2021
    },
    "child2" : {
        "name" : "Lucy",
        "year" : 2022
    },
    "child3" : {
        "name" : "riku",
        "year" : 2025
    }
}
print(myfamily)

#we can write like this also
child1 = {
        "name" : "Rio",
        "year" : 2021
}
child2 = {
        "name" : "Lucy",
        "year" : 2022
}
child3 = {
        "name" : "riku",
        "year" : 2025
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3 
}
print(myfamily)


#Access items in nested dictionary
child1 = {
        "name" : "Rio",
        "year" : 2021
}
child2 = {
        "name" : "Lucy",
        "year" : 2022
}
child3 = {
        "name" : "riku",
        "year" : 2025
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3 
}
print(myfamily["child2"]["year"])

#Loop through nested dictionaries
child1 = {
        "name" : "Rio",
        "year" : 2021
}
child2 = {
        "name" : "Lucy",
        "year" : 2022
}
child3 = {
        "name" : "riku",
        "year" : 2025
}
myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3 
}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y  + ':', obj[y])

#Dictionary Comprehension
nums = [1, 2, 3, 4]
squares = {n: n**2 for n in nums}
print(squares)

#Convert list of tuples into dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = {k: v for (k, v) in pairs}
print(d)

#Filtering with condition
nums = range(10)
evens = {n: n**2 for n in nums if n % 2 == 0}
print(evens)

#Without comprehensions
nums = [1, 2, 3, 4]
squares = {}
for n in nums:
    squares[n] = n**2
print(squares)

#With comprehensions
nums = [1, 2, 3, 4]
squares = {n: n**2 for n in nums}
print(squares)