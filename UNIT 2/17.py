#P_7 Write a program to demonstrate list dictionary and set comprehensions.

#list comprehensions
numbers = [1,2,3,4,5]
square_list=[x*x for x in numbers]

print("Original list :",numbers)
print("Square list :",square_list)

#Dictionary comprehension

square_dict={x: x*x for x in numbers}

print("\n Dictionary")
print(square_dict)

#set comprehension
square_set ={x*x for x in numbers}

print("\n set")
print(square_set)

