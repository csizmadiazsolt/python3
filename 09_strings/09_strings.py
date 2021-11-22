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
