#! /usr/bin/env python3.7

while True:
    try:
        value = int(input("Please enter a number: "))
    except ValueError:
        print("Your input could not be converted to an integer.")
        continue

    break

print(value)
