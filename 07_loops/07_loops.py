#!/usr/bin/python3

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

# Infinite loop
var = 1
while var == 1:
    num = int(input("Enter a number: "))
    print("Your number is: " + str(num))