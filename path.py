import os

# Ask the user to enter the path of the directory
directory_path = input("Enter the directory path: ")

# Check if the path is a valid directory
if os.path.isdir(directory_path):
    print(f"\nContents of '{directory_path}':")
    for item in os.listdir(directory_path):
        print(item)
else:
    print("The path you entered is not a valid directory.")
