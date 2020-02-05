#! /usr/bin/env python3.7


def is_all_digits(s):  # s is a formal paramter
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for character in s:
        if character not in digits:
            return False

    return True


my_string = "1a2b3c"

result = is_all_digits(my_string)  # my_sting is an actual parameter

print(result)
