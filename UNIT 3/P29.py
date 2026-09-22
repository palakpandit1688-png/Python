#Write a program to use re module functions such as match search and findall.

import re

text = input("Enter text : ")

# match()
result = re.match(r"\w+", text)

if result:
    print("match(): Text starts with =", result.group())
else:
    print("match(): Text does not start with a word")

# search()
result = re.search(r"\w+", text)

if result:
    print("search(): Word found =", result.group())
else:
    print("search(): Word not found")

# findall()
words = re.findall(r"\w+", text)
print("findall():", words)
