#! /usr/bin/env python3.7

import timeit

COUNT = 10_000_000


def using_map():
    return sum(map(lambda i: i * i, range(COUNT)))


def using_comprehension():
    return sum([i * i for i in range(COUNT)])


def using_for_loop():
    sum_ = 0
    for i in range(COUNT):
        sum_ += i * i
    return sum_


def using_generator():
    return sum(i * i for i in range(COUNT))


if __name__ == "__main__":
    print()
    print(f"Summing the squares of the first {COUNT:,} integers...")

    with_map = timeit.timeit(using_map, number=100)
    print(f"{with_map:>.5f} seconds (map())")

    with_comprehension = timeit.timeit(using_comprehension, number=100)
    print(f"{with_comprehension:>.5f} seconds (list comprehension)")

    with_loop = timeit.timeit(using_for_loop, number=100)
    print(f"{with_loop:>.5f} seconds (for loop)")

    with_generator = timeit.timeit(using_generator, number=100)
    print(f"{with_generator:>.5f} seconds (generator)")

    # Summing the squares of the first 1,000,000 integers...
    # 6.58681 seconds (map())
    # 7.93916 seconds (list comprehension)
    # 5.44238 seconds (for loop)
    # 5.18300 seconds (generator)

    # Summing the squares of the first 10,000,000 integers...
    # 76.48243 seconds (map())
    # 108.90998 seconds (list comprehension)
    # 60.98440 seconds (for loop)
    # 61.87536 seconds (generator)
