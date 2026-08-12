#Write a program to demonstrate different import mechanisms in Python.

# 1. Import entire module
import math

print("Square root =", math.sqrt(25))


# 2. Import specific function
from math import factorial

print("Factorial =", factorial(5))


# 3. Import multiple functions
from math import pow, ceil

print("Power =", pow(2, 3))
print("Ceil =", ceil(4.2))


# 4. Import module with an alias
import math as m

print("Value of PI =", m.pi)
