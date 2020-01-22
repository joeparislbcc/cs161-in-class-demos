#! /usr/bin/env python3.7
import time

count = 10  # loop control varialbe

while count > 0:  # test loop condition
    time.sleep(0.5)
    count -= 1  # modify the loop control variable
    if count == 5:
        continue
    print(f"{count}...")

print("🚀  Blast off!! 🚀")
