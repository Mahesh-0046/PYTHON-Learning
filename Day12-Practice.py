#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates not allowed
thisset = {"apple", "banana", "cherry", "apple"} #Set ignores the duplicate values
print(thisset)

#True and 1 considered as same so its a duplicate
thisset = {"apple", "banana", "cherry", True, 1, 2} 
print(thisset)

#False and 0 considered as same so its a duplicate
thisset = {"apple", "banana", "cherry", False, 1, 0} 
print(thisset)

#Add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Add sets
thisset = {"apple", "banana", "cherry"}
fruits = {"orange", "pineapple", "guava"}
thisset.update(fruits)
print(thisset)

#Add any iterable (update())
thisset = {"apple", "banana", "cherry"}
thislist = ["orange", "pineapple", "guava"]
thisset.update(thislist)
print(thisset)

#Remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

#Remove by using discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Remove by using pop() but it removes random
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #randomly it removes banana this time
print(thisset)

#Clear (this will empty the set)
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

"""Del keyword
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) #this variable does not exist in the storage"""

#Loop set
thisset = {"apple", "banana", "cherry"}
for i in thisset:
    print(i)
    
#Join Sets
#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# we can use | operator instead of union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"x", "y", "z"}
set4 = {4, 5, 6}
myset = set1.union(set2, set3, set4)
print(myset)

#(or)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"x", "y", "z"}
set4 = {4, 5, 6}
myset = set1 | set2 | set3 | set4
print(myset)

#Join a Set and a tuple
set1 = {"a", "b", "c"}
tuple1 = ("d", "e", "f")
myset = set1.union(tuple1)
print(myset)

#Update
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#Intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1.intersection(set2)
print(set3)

# we can use & instead od intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1 & set2
print(set3)

#Intersection_update
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set1.intersection_update(set2)
print(set1)

#Difference
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1.difference(set2)
print(set3)

#instead of difference we can use - operator
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1 - set2
print(set3)

#Difference_update
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set1.difference_update(set2)
print(set1)

#Symmetric_difference
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#we can use ^ instead of Symmetric_difference
set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "google", "gemini", "apple"}
set3 = set1 ^ set2
print(set3)

#frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
