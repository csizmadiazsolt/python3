#!/usr/bin/python3

# If statement
a = True
b = False
if a:
    print("True statement!")

if b:
    print("True statembet!")

print("Good bye!")

# If..else statement
amount = int(input("Enter amount: "))

if amount < 1000:
    print("Less than 1000")
elif amount >= 1000 and amount < 2000:
    print("Between 1000 and 2000")
elif amount >= 2000 and amount < 3000:
    print("Between 2000 and 3000")
else:
    print("Over 3000")

# Nested if statement
if amount < 1000:
    if amount < 500:
        print("Less than 500")
        if amount < 300:
            print("Less than 300")
    else:
        print("More than 500, but less than 1000")
else:
    print("Over 1000")

# One-line if clause
a = 100
if a == 100 : print("One-liner!")

# Simple switch-case in Python
def week(i):
    switch_options = {
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday"}
    
    return switch_options.get(i, "Invalid day of week!")

print(week(1))
print(week(3))
print(week(15))