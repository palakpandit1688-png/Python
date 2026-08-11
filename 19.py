#Write a program to demonstrate iterators and iterables in Python.

# Iterable
fruits = ["Apple", "Mango", "Banana"]

print("Iterable:")
for fruit in fruits:
    print(fruit)

# Convert iterable into iterator
fruit_iterator = iter(fruits)

print("\nIterator:")
print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))
