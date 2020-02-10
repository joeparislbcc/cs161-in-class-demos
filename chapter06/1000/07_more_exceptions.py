#! /usr/bin/env python3.7

try:
    # with this two-step process, value will be assigned the input
    value = input("Please enter an integer: ")
    value = int(value)
except ValueError:
    print(f"Your input, {value}, could not be cast to int.")
except NameError:
    print(f"Bad variable name {value}.")

print(value)
