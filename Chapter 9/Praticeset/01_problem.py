# Write a program to read the text from a given file "poem.txt" and find out whether it contains the word "twinkle"
import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "poem.txt")

with open(file_path, "r") as f:
    content = f.read()

if "Twinkle" in content:
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")