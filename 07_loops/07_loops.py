#!/usr/bin/python3

import sys

# While loop
count = 0
while count < 9:
    print("The count is: " + str(count))
    count = count + 1
else:
    print("The while loop is over.")

# For loop with range
for var in range(5):
    print(str(var))

# For loop with lists
list1 = ["apple", "banana", 56]
for var in list1:
    print(str(var))

# For loop with Strings
for var in "Apple pie":
    print(str(var))

# Iterate by sequence index
list2 = ["origo", "pentagon", "abstract"]
for index in range(len(list2)):
    print(str(list2[index]))

# For loop with else statement
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num%2 == 0:
      print ("The list contains an even number.")
      break
else:
   print ("The list doesnot contain even number.")

# Nested for loop
for i in range(1,11):
    for j in range(1,11):
        k = i * j
        print(k, end=' ')
    print()

# Break statement
for i in range(10):
    if i == 4:
        break
    print("Next number", i)

# Continue statement
for i in range(10):
    if i == 4:
        continue
    print("Next number", i)

# Pass statement
for i in range(10):
    if i == 4:
        pass
        print("This is a pass block")
    print("Next number", i)

# Iterator with for loop
list1 = [1, 2, 7, 8, 11]
it = iter(list1)

for i in it:
    print(i, end=" ")

print()

# Iterator with while loop
list2 = [2, 4, 14, 16, 22]
it = iter(list2)

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        print()
        break

# Generator
def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

f_iterator = fibonacci(10)

while True:
   try:
      print (next(f_iterator), end=" ")
   except StopIteration:
      print()
      break

# Infinite loop
var = 1
while var == 1:
    try:
        num = int(input("Enter a number: "))
    except KeyboardInterrupt:
        print("You've pressed something else...")
        sys.exit()
    except ValueError:
        print("This is not a valid integer...")
        sys.exit()
    print("Your number is: " + str(num))