#Write a program to demonstrate basic regular expression pattern matching.

#Check mobile number
import re

mobile = input("Enter your mobile number: ")

pattern = r"^[0-9]{10}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
