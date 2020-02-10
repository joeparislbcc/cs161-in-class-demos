#! /usr/bin/env python3.7

# use a context manager to control opening and closing of files
with open("temp.txt", "r") as temp_file:
    for line in temp_file:
        text_line = line.strip()
        print(text_line)

# Python will automatically close the file now
