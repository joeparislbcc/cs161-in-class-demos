#! /usr/bin/env python3.7

"""Demonstrate if"""

value = int(input("Please enter an integer: "))

if value % 2 == 0:
    # if value is an even number execute this suite of code
    print(f"{value} is even.")
elif value % 3 == 0:
    print(f"{value} is divisible by 3.")
elif value % 5 == 0:
    print(f"{value} is divisible by 5.")
elif value % 6 == 0:
    print(f"{value} is divisible by 6.")
else:
    print(f"{value} is not divisible by 2, 3, 5, or 6.")

print("Thanks for giving me a number.")

# you can have exactly 1 "if" statement, followed by 0 or more
# elif statements, optionally followed by 0 or 1 else statement
