#! /usr/bin/env python3.7

total = 0

while True:
    file_name = input("Please enter the name of file that contains numbers to add: ")
    try:
        with open(file_name, "r") as in_file:
            for num in in_file:
                try:
                    total += int(num)
                except ValueError:
                    # print an error message?? && break
                    continue
    except FileNotFoundError:
        print(f"file {file_name} not found.")
    except:
        # catch all errors that aren't handled above
    else:
        print(total)
        break

print("Done!")
