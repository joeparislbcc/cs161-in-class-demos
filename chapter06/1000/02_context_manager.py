#! /usr/bin/env python3.7

# use a context manager to open and manage the file for us
with open("text.txt") as input_file:
    for text in input_file.readlines():
        print(text.strip())

# at this point the context manager will have closed the file for us
