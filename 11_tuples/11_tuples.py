#!/usr/bin/python3

tuple1 = ('apple', 'banana', 1997, 2000)
tuple2 = (1, 22, 333, 4444)

print("tuple1[0]: ", tuple1[0])
print("tuple2[0:3]: ", tuple2[0:3])

# Cannot update tuple
print("Value at index 2:", tuple1[2])

try:
    tuple1[2] = 'MR. UPDATE'
except TypeError:
    print("'tuple' object does not support item assignment!")

# Length of tuple
print("Length:", len(tuple1))

# Tuple concatenation
tuple3 = tuple1 + tuple2
print("Concatenated lists - tuple1 + tuple2", tuple3)

# Tuple membership
print('apple' in tuple1)
print('mango' in tuple1)

# Repetition
print('Repete twice:', tuple1 * 2)

# Iteration
for i in tuple1:
    print(i, end=" ")

# Delete tuple
del tuple1
try:
    print("tuple1 after deletion", tuple1)
except NameError:
    print("name 'tuple1' is not defined.")

# Return max and min value
tuple4 = (1, 56, 684, 3, 31)
print("max(tuple4):", max(tuple4))
print("min(tuple4):", min(tuple4))

# Count
print('tuple4.count(684):', tuple4.count(684))

# Index
print('tuple4.index(684):', tuple4.index(684))

# Convert list to tuple
list1 = [1, 2, 3, 63]
tuple1 = tuple(list1)
print('Tuple elements:', tuple1)
