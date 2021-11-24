#!/usr/bin/python3

list1 = ['apple', 'banana', 1997, 2000]
list2 = [1, 22, 333, 4444]

print("list1[0]: ", list1[0])
print("list2[0:3]: ", list2[0:3])

# Update list element
print("Value at index 2:", list1[2])

list1[2] = 'MR. UPDATE'
print("Updated value at index 2:", list1[2])

# Delete list element
del list1[2]
print("list1 after deletion", list1)

# Length of list
print("Length:", len(list1))

# List concatenation
list3 = list1 + list2
print("Concatenated lists - list1 + list2", list3)

# List membership
print('apple' in list1)
print('mango' in list1)

# Repetition
print('Repete twice:', list1 * 2)

# Iteration
for i in list1:
    print(i, end=" ")

# Return max and min value
print()
list4 = [1, 56, 684, 3, 31]
print("max(list4):", max(list4))
print("min(list4):", min(list4))

# Append
list4.append(684)

# Count
print('list4.count(684):', list4.count(684))

# Extend
list5 = range(5)
list4.extend(list5)
print('Extended list:', list4)

# Index
print('list4.index(684):', list4.index(684))

# Insert
list4.insert(0, 999)
print('list4.instert(0,999): ', list4)

# Remove
list4.remove(684)
list4.remove(684)
print('list4 after removal:', list4)

# Reverse
list4.reverse()
print('Reverse list:', list4)

# Sort
list4.sort()
print('Sorted list:', list4)
