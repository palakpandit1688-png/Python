#Write a program to generate random numbers using random module.

import random

# Random number
print("Random Number =", random.randint(1, 100))

# Random decimal
print("Random Decimal =", random.random())

# 5 random numbers
print("5 Random Numbers:")
for i in range(5):
    print(random.randint(1, 100))

# Random subject
subjects = ["Python", "DBMS", "Java", "Maths", "Computer"]
print("Random Subject =", random.choice(subjects))

# Generate OTP
otp = random.randint(100000, 999999)
print("Generated OTP =", otp)
