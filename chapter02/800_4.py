#! /usr/bin/env python3.7

# validate user input
while True:
    value = int(input("Please enter an integer between 1 and 10: "))
    if value >= 1 and value <= 10:
        break
    print(f"Sorry, {value} is not between 1 and 10. Please try again.")

print(f"Thanks for giving me a {value}.")
