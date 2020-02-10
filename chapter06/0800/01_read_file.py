#! /usr/bin/env python3.7

temp_file = open("temp.txt", "r")

for line in temp_file:
    text_line = line.strip()
    print(text_line)

temp_file.close()  # always close your files when you are done
