#!/usr/bin/python3

dict1 = {'name': 'Zsolti', 'age': 33, 'salary': 5}
print("dict1['name']:", dict1['name'])
print("dict1['age']:", dict1['age'])

# Update dictionary
dict1['name'] = 'Tobias'
dict1['age'] = 42
print("dict1['name']:", dict1['name'])
print("dict1['age']:", dict1['age'])

del dict1['name']
print("dict1:", dict1)
dict1.clear()
print("dict1.clear:", dict1)
del dict1

try:
    print("dict1", dict1)
except NameError:
    print("name 'dict1' is not defined.")

# Compare dictioneries
dict1 = {'Name': 'Zsolti', 'Age': 33}
dict2 = {'Name': 'Adri', 'Age': 34}
dict3 = {'Name': 'Zsolti', 'Age': 33}
print("Return Value :", dict1 == dict2)
print("Return Value :", dict1 == dict3)

# Length of a dictionary
print('len(dict1):', len(dict1))

# Dictionary to string
print('str(dict1):', str(dict1))

# Define type
print("Variable Type:", type(dict1))

# Clear dictionary
print('Length before clean:', len(dict3))
dict3.clear()
print('Length after clean:', len(dict3))

# Copy dictionaries
dict4 = dict1.copy()
print('dict4 after copying dict1:', dict4)

# Get for dictionary
print("dict4.get('Name'):", dict1.get('Name'))
print("dict4.get('Sex'):", dict1.get('Sex'))

# Membership
print("'Age' in dict1:", 'Age' in dict1)
print("'Sex' in dict1:", 'Sex' in dict1)

# Items: returns tuple pairs
print("Key and value pairs:", dict1.items())

# Keys: returns a list
print("Keys:", dict1.keys())

# Values: returns a list
print("Values:", dict1.values())

# Set default value
dict1.setdefault("Sex", None)
print("dict1 after setting default values:", dict1)

# Update a dictionary by another
dict1 = {'name': 'Zsolti', 'age': 33, 'salary': 5}
dict2 = {'sex': 'male'}
dict1.update(dict2)
print("dict1 after update by dict2:", dict1)
