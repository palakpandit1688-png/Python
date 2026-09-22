#Write a program to generate a sequence of numbers using generator functions and yield keyword.

# using generator function and yield keyword
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Calling generator function
numbers = generate_numbers(10)

print("Sequence of numbers:")

for num in numbers:
    print(num)
