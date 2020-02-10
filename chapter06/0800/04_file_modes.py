#! /usr/bin/env python3.7

# use a context manager to control opening and closing of files
with open("temp.txt", "r") as in_file, open("out2.txt", "a") as out_file:
    for _ in range(3):
        text = input("Please enter some text: ")
        out_file.write(text)
        out_file.write("\n")

# Python will automatically close the file now
