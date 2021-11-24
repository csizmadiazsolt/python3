#!/usr/bin/python3

import base64

var1 = "Hello Zsolti!"
print("var1[0] :", var1[0])
print("var1[1:4] :", var1[1:4])
print("Update string :", var1[:6] + "Python!")

# Escape characters
print("\a", end="")
print("\b", end="")
print("\f", end="")
print("Line1\nLine2")
print("ABCDEFG\r123")
print("A\tB\tC\t")
print("A\vB\vC")

# String formatting
print("Hello,\nMy name is %s, I'm %d years old and my weight is %d kg." %
      ('Zsolti', 33, 70))
print("Oh and this a floating point number %f" % (45.23))
print("A %-12s B" % ('Zsolti'))
print("A %+12s B" % ('Zsolti'))

# Triple quotes
var2 = """This is a wonderful example
how to use \t three quotation marks and
put everything into new lines and\n\b
print it in the same fashion..."""
print(var2)

# Raw string
print("C:\\Folder")
print(r"C:\\Folder")

# Capitalize
str1 = "zsolti"
print("str1.capitalize() :", str1.capitalize())

# Center
print("str1.center(40, '_') :", str1.center(40, '_'))

# Encode
str2 = "Zsolti's string to be encoded"
str2 = str2.encode('UTF-8', 'strict')
print("Encoded:", str2)
print("Decoded:", str2.decode('UTF-8', 'strict'))

# Some other methods
print("str1.capitalize() :", str1.capitalize())

str2 = "Zsolti's string to be encoded"
print("str2.count('i') : ", str2.count('i'))
print("str2.count('i', 1, 7) : ", str2.count('i', 1, 7))
print("str2.count('i', 1, 4) : ", str2.count('i', 1, 4))

print(str2.endswith('ded'))
print(str2.endswith('ded', 20))
print(str2.endswith('ded', 0, 20))

print(str2.find('encoded'))
print(str2.find('encoded', 10))
print(str2.find('encoded', 10, 15))

try:
    print(str2.index('encoded', 10, 15))
except ValueError:
    print("substring not found")

print(str1.isalnum())
print(str2.isalnum())

print(str1.isalpha())
print(str2.isalpha())

str2 = "4567"
print(str2.isnumeric())

print("Length of the string :", len(str1))

str2 = "THIS IS AMAZING!"
print("str2.lower :", str2.lower())

str2 = "this is amazing!"
print("str2.upper :", str2.upper())

print(str2.split())
print(str2.split('i', 2))
