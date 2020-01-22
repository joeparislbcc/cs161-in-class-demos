#! /usr/bin/env python3.7

value = int(input("Enter an integer: "))

if value % 2 == 0:
    print(f"{value} is evenly divisible by 2.")
elif value % 5 == 0:
    print(f"{value} is evenly divisible by 5.")
elif value % 3 == 0:
    print(f"{value} is evenly divisible by 3.")
elif not value % 7 == 0 and value % 11 == 0:
    print(f"{value} is divisible by both 7 and 11.")

# you can use the Python operators and, or, not to combine Boolean expressions
# in your decision structures and also in iterative structures
