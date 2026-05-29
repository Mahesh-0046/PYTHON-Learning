# Print numbers 1 to 20

for i in range(1, 21):
    print(i)


# While loop counter
count = 1

while count <= 10:
    print(count)
    count += 1


# break example
for i in range(1, 11):
    if i == 7:
        break
    print(i)

print("-----")

# continue example
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Pattern 1
for i in range(1, 6):
    print("*" * i)

print("-----")

# Pattern 2 (reverse)
for i in range(5, 0, -1):
    print("*" * i)


# Sum of 1 to n

n = int(input("Enter number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# Sum of even numbers 1 to 100
even_sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i

print("Even Sum:", even_sum)


# Average of n numbers
n = int(input("How many numbers: "))
total = 0

for i in range(n):
    num = int(input("Enter number: "))
    total += num

avg = total / n
print("Average:", avg)