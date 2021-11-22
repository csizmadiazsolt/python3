#!/usr/bin/python3

import math
import random

# Some math functions
print("abs(-45) : ", abs(-45))
print("ceil(45.23)", math.ceil(45.23))
print("ceil(-45.23)", math.ceil(-45.23))
print("math.exp(2.17) : ", math.exp(2.17))
print("math.exp(math.pi) : ", math.exp(math.pi))
print("math.fabs(-45.23) : ", math.fabs(-45.23))
print("floor(45.23)", math.floor(45.23))
print("max(80, 100, 1000) : ", max(80, 100, 1000))
print("min(80, 100, 1000) : ", min(80, 100, 1000))
print("math.pow(100, 2) : ", math.pow(100, 2))

# Choice
print("Returns a random number from range(100) : ", random.choice(range(100)))
print("Returns a random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print("Returns a random character from string 'Hello World' : ", random.choice("Hello World"))

# Randomly select an odd number between 1-100 
print("randrange(1, 100, 2) : ", random.randrange(1, 100, 2))

# Random between 0 and 1
print("random() : ", random.random())

# Random with seed
random.seed("hello", 2)
print("Random number with string seed : ", random.random())

# Shuffle
random.seed()
list = [20, 16, 10, 5]
print("Original list : ",  list)

random.shuffle(list)
print("Reshuffled list : ",  list)

# Random uniform float
print("Random Float uniform(5, 10) : ",  random.uniform(5, 10))

# Mathematic constants
print("pi : ", math.pi)
print("e : ", math.e)

# Some trigonometric functions
print("sin(3) : ",  math.sin(3))
print("sin(math.pi/2) : ",  math.sin(math.pi/2))
print("cos(2*math.pi) : ",  math.cos(2*math.pi))
print("tan(math.pi/4) : ",  math.ceil(math.tan(math.pi/4)))