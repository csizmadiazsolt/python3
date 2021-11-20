#!/usr/bin/python3

# Arithmetic operators
a = 23
b = 42
c = 0

c = a + b
print(str(a) + " + " + str(b) + " = " + str(c))

c = a - b
print(str(a) + " - " + str(b) + " = " + str(c))

c = a * b
print(str(a) + " * " + str(b) + " = " + str(c))

c = a / b
print(str(a) + " / " + str(b) + " = " + str(c))

c = a % b
print(str(a) + " % " + str(b) + " = " + str(c))

a = 2
b = 3
c = a**b
print(str(a) + " ** " + str(b) + " = " + str(c))

c = b//a
print(str(b) + " // " + str(a) + " = " + str(c))

# Comparision operators
a = 6
b = 9
c = a == b
print(str(a) + " == " + str(b) + " = " + str(c))

c = a != b
print(str(a) + " != " + str(b) + " = " + str(c))

c = a > b
print(str(a) + " > " + str(b) + " = " + str(c))

c = a < b
print(str(a) + " < " + str(b) + " = " + str(c))

c = a >= b
print(str(a) + " >= " + str(b) + " = " + str(c))

c = a <= b
print(str(a) + " <= " + str(b) + " = " + str(c))

# Assignment operators
a = 0
print(str(a))

a = 21 + 32
print(str(a))

a += 11
print(str(a))

a -= 11
print(str(a))

a *= 2
print(str(a))

a /= 2
print(str(a))

a **= 3
print(str(a))

a //= 2
print(str(a))

a %= 3
print(str(a))

# Bitwise operators
a = 60
b = 13

print("a= " + str(a) + " : " + bin(a))
print("b= " + str(b) + " : " + bin(b))

c = a & b
print("AND: a & b=" + str(c) + " : " + bin(c))

c = a | b
print("OR: a | b=" + str(c) + " : " + bin(c))

c = a ^ b
print("EXOR: a ^ b=" + str(c) + " : " + bin(c))

c = ~ a
print("COMPLEMENT: ~a=" + str(c) + " : " + bin(c))

c = a << 2
print("LEFT SHIFT: a << 2=" + str(c) + " : " + bin(c))

c = a >> 2
print("RIGHT SHIFT: a >> 2=" + str(c) + " : " + bin(c))

# Logical operators
a = True
b = False

c = a and b
print(str(a) + " and " + str(b) + " = " + str(c))

c = a or b
print(str(a) + " or " + str(b) + " = " + str(c))

c = not b
print("not " + str(b) + " = " + str(c))

# Membership operators
a = ("apple", "banana", "mango")
b = "apple"

c = b in a
print(str(b) + " in " + str(a) + " = " + str(c))

c = b not in a
print(str(b) + " not in " + str(a) + " = " + str(c))

# Identity operators
a = ["this", "list"]
b = ["this", "list"]
c = a

print(a is b)
print(a is c)
print(c is a)
print(b is c)
print(a is not c)