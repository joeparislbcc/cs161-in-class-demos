#! /usr/bin/env python3.7

"""Input validation: numbers in a range."""

while True:
    value = int(input("Please enter an int between 1 and 10 inclusive: "))
    # if value >= 1 and value <= 10:
    # if value in [28, 29, 30, 31]:
    if value in range(1, 11):
        break

    print(f"{value} is not in the range 1 to 10 inclusive.")

print(f"The value you entered was {value}.")
