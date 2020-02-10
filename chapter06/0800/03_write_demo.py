#! /usr/bin/env python3.7

# use a context manager to control opening and closing of files
with open("temp.txt", "r") as in_file:
    with open("out.txt", "w") as out_file:
        for line in in_file:
            line = line.strip().upper()
            print(line, file=out_file)  # redirect print() to file rather than screen
            # out_file.write(line)
            # out_file.write("\n")

# Python will automatically close the file now
