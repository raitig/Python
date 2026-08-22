import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "file.txt")

with open(file_path, "r") as f:
    data = f.read()

print(data)