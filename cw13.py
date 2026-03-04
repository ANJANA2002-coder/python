# items_file_program.py

import os

filename = "items.txt"

# Step 1: Ask user for new item
item = input("Enter the name of the new item: ")

# Step 2: Check if file exists
if not os.path.exists(filename):
    # File does not exist → create and write
    with open(filename, "w") as file:
        file.write(item + "\n")
    print("File created and item added.")
else:
    # File exists → append item
    with open(filename, "a") as file:
        file.write(item + "\n")
    print("Item added to existing file.")

# Step 3: Display full list of items
print("\nFull list of items:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())