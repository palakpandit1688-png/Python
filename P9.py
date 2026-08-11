#Write a program to define and use user-defined functions with different types of arguments.


#Function with no argument
def welcome():
    print("Welcome to Python")

#Function with positional arguments
def add(a, b):
    print("Addition =", a + b)

#Function with default argument
def greet(name="Palak"):
    print("Hello", name)

#Function with keyword arguments
def student(name, age):
    print("Name =", name)
    print("Age =", age)

#Function with variable-length arguments
def total(*numbers):
    print("Total =", sum(numbers))


#Function calls
welcome()

add(10, 20)

greet()

student(age=20, name="Palak")

total(10, 20, 30, 40)
