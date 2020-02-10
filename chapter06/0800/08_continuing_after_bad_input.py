#! /usr/bin/env python3.7

print("Let's add some numbers.")

try:
    file_name = input("Please enter the name of a file containg some numbers: ")

    with open(file_name, "r") as in_file:
        total = 0
        for num in in_file:
            try:
                total += int(num)
            except ValueError:
                # print("Invalid input from file.")
                continue
except FileNotFoundError:
    print(f"File {file_name} not found.")
else:
    print(total)
