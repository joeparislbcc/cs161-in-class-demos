#! /usr/bin/env python3.7

try:
    value = int(input("Please enter an integer: "))
except:
    print(f"Your input, {value}, could not be cast to int.")

print(value)
