#String

print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

#Multiline String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

A = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Loop
for x in "banana":
    print(x)

#String length
a = "Hello, World"
print(len(a))

#Check string
txt = "The best things in life are free!"
print("free" in txt)

#Slicing
b = "Hello, World"
print(b[2:5])

b = "Hello, World"
print(b[:5])

b = "Hello, World"
print(b[5:])

b = "Hello, World"
print(b[-5:-2])

b = "Hello, World"
print(b[::2])

#Upper case
a = "Hello, World!"
print(a.upper())

#Lower case
a = "Hello, World!"
print(a.lower())

#Remove Whitespaces
a = "Hello, World!"
print(a.strip())

#Replace string
a = "Hello, World!"
print(a.replace("H", "J"))

#Split string
a = "Hello, World"
print(a.split(","))

#Find String
txt = "Hello, welcome to my world"
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world"
x = txt.find("e", 5, 10)
print(x)

#Count String
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

