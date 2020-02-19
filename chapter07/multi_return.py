#! /usr/bin/env python3.7


def func(*args, num1=1, num2=1):
    """Return only even parameters."""
    # return_values = []

    # if x % 2 == 0:
    #     return_values.append(x)

    # if y % 2 == 0:
    #     return_values.append(y)

    # if z % 2 == 0:
    #     return_values.append(z)

    # return return_values

    return [n for n in args if n % num1 == 0 and n % num2 == 0]


if __name__ == "__main__":
    vals = func(2, 3, 4)
    print(vals)

    vals = func(5, 7, 8)
    print(vals)

    vals = func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, num1=3)
    print(vals)

    vals = func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, num1=3, num2=4)
    print(vals)
