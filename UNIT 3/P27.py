#Write a program to copy move and delete files using shutil module.

import shutil
import os

# Copy
shutil.copy("test.txt", "copy.txt")
print("File copied")

# Move
shutil.move("copy.txt", "moved.txt")
print("File moved")

# Delete
os.remove("moved.txt")
print("File deleted")
