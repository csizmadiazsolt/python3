#!/usr/bin/python3

# Numbers and variables
num1 = num2 = 1
num3 = -10
num4 = 0.5
num5 = 3.14j
one, two = 1, "two"

# Strings
str1 = "python string"

print(str1)
print(str1[2])
print(str1[2:])
print(str1[2:5])
print(str1 * 2)
print(str1 + ", isn't it wonderful?")

# Object deletion
del str1

try:
    print(str1)
except NameError:
    print("NameError: name 'str1' is not defined.")

# Lists
list1 = ['apple', 2, 2.75, 'johnny']
list2 = ['dude', 54]

print(list1[2])
print(list1[2:])
print(list1[2:3])
print(list1 * 2)
print(list1 + list2)

# Tuples
tuple1 = ('apple', 2, 2.75, 'johnny')
tuple2 = ('dude', 54)

print(tuple1[2])
print(tuple1[2:])
print(tuple1[2:3])
print(tuple1 * 2)
print(tuple1 + tuple2)

# Tuple assignment doesn't work!
try:
    tuple1[1] = 45
except TypeError:
    print("'tuple' object does not support item assignment!")

# Dictionaries
dict1 = {}
dict1['one'] = 1
dict1['2'] = "two"

dict2 = {'name' : 'Tobias', 'age' : 45, 'salary' : 1200}

print(dict1['one'])
print(dict2.keys())
print(dict2.values())

# Sets
set1 = {"apple", "juice", "cocktail", "armageddon", 123, "armageddon", 123}
print(set1)
print(len(set1))
print("apple" in set1)
print("cockroach" in set1)

# Set assignment doesn't work!
try:
    set1[1] = "45"
except:
    print("'set' object does not support item assignment!")

# Some conversions...
int("100")
float("45.2")
str(100)
list("Apple pie")
tuple("Cow pie")
hex(100)