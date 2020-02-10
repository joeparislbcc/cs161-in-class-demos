#! /usr/bin/env python3.7

# TODO: fix example

try:
    try:
        value = int(input("Please enter an integer: "))
    except ValueError:
        print(f"Your input, {value}, could not be cast to int.")
except NameError:
    print(f"Bad variable name {value}.")

print(value)
