#! /usr/bin/env python3.7

input_file = open("text.txt")

for text in input_file.readlines():
    print(text.strip())

# close the file
input_file.close()
