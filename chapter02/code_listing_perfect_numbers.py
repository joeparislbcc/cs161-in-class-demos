#! /usr/bin/env python3.7

print("Find the first 10 perfect numbers.")

count = 1
number = 1

while count <= 10:
    divisor = 1
    sum_of_divisors = 0
    while divisor < number:
        if number % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1

    if number == sum_of_divisors:
        print(f"Perfect number #{count} is {number}")
        count += 1
    number += 1
