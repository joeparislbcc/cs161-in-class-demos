#! /usr/bin/env python3.7

value = int(input("Please enter a number: "))

if value % 2 == 0:  # is value an even number?
    print(f"{value} is even.")
    print("we're in the if's suite")
    print("still in there!")
else:  # executes when value is odd
    print(f"{value} is odd.")
    print("we're in the else's suite")


print("Done running the program.")
