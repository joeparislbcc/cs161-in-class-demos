#! /usr/bin/env python3.7

# greeting = "Jello world"

# print(greeting)  # greeting is an actual parameter

# print()


def is_all_digits(s):  # s is a formal paramter
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for character in s:
        if character not in digits:
            return False

    return True


my_string = "1a2b3c"

is_all_digits(my_string)  # my_sting is an actual parameter


def divide_numbers(numerator, denominator):  # numerator and denominator are formal parameters
    return numerator / denominator  # return 37 / 42


a = 37
b = 42


dividend = divide_numbers(b, a)


def gndn():
    return 3 + 7


answser = gndn()

print(answser)
