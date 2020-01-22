#! /usr/bin/env python3.7
"""Plot Collatz conjecture for a given integer."""

import pylab

value = int(input("Please enter a starting value: "))
sequence = [value]

while value > 1:
    if not value % 2 == 0:
        value = value * 3 + 1
    else:
        value //= 2

    sequence.append(value)

print(sequence)
pylab.title(f"Collatz Conjecture Series for {sequence[0]}")
pylab.grid(True)
pylab.xlabel("Iteration")
pylab.ylabel("Value")
pylab.plot(sequence)
pylab.show()
