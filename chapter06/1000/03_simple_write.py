#! /usr/bin/env python3.7

# use a context manager to open and manage the file for us
with open("out1.txt", "w") as out_file:
    string = input("Please enter some text: ")

    out_file.write(string + "\n")

# at this point the context manager will have closed the file for us
