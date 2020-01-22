#! /usr/bin/env python3.7

import time

print("Squares:")

for value in range(1, 11):
    print(f"{value} => {value ** 2}")
    time.sleep(0.25)
