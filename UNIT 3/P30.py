#Write a program to extract specific information from a text file using regular expressions.

import re

# Open file
file = open("data.txt", "r")
text = file.read()
file.close()

# Extract email
email = re.findall(r'\S+@\S+', text)

# Extract phone number
phone = re.findall(r'\d{10}', text)

print("Email:", email)
print("Phone:", phone)
