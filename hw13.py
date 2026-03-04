import os

filename = "students.txt"
num = int(input("How many student names do you want to add? "))

if os.path.exists(filename):
    print("\nExisting student names:")
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print("\nNo existing file found. A new file will be created.")

with open(filename, "a") as file:
    for i in range(num):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

print("\nUpdated list of student names:")
with open(filename, "r") as file:
    print(file.read())