#! /usr/bin/env python3.7
"""First plot."""
import pylab

nums = []
for counter in range(10):
    nums.append(counter * 2)

print(nums)
print(len(nums))

# now plot the list
pylab.plot(nums)
pylab.show()
