import os
import sys

# Take input from user
folder = input("Enter directory name: ")
filename = input("Enter file name: ")

# Create directory
os.mkdir(folder)
#Write a program to perform file and directory operations using os and sys modules
print("Directory created:", folder)

# Create file
filepath = os.path.join(folder, filename)

with open(filepath, "w") as file:
    file.write("Hello Python")

print("File created:", filename)

# Display directory contents
print("Contents:", os.listdir(folder))

# Rename file
newname = input("Enter new file name: ")
newpath = os.path.join(folder, newname)

os.rename(filepath, newpath)
print("File renamed to:", newname)

# Delete file
os.remove(newpath)
print("File deleted")

# Delete directory
os.rmdir(folder)
print("Directory deleted")

# Display program name
print("Program name:", sys.argv[0])
