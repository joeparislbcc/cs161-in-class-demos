#! /usr/bin/env python3.7

import random
import timeit

TAX_RATE = 0.08
ITEMS = 100_000
txns = [random.randrange(100) for _ in range(100_000)]


def get_price(txn):
    return txn * (1 + TAX_RATE)


def get_prices_with_map():
    return list(map(get_price, txns))


def get_prices_with_comprehension():
    return [get_price(txn) for txn in txns]


def get_prices_with_loop():
    prices = []
    for txn in txns:
        prices.append(get_price(txn))
    return prices


if __name__ == "__main__":
    print()
    print(f"Comparing run times for calculating sales tax on {ITEMS:,} items...")

    with_map = timeit.timeit(get_prices_with_map, number=100)
    print(f"{with_map:>.5f} seconds (map())")

    with_comprehension = timeit.timeit(get_prices_with_comprehension, number=100)
    print(f"{with_comprehension:>.5f} seconds (list comprehension)")

    with_loop = timeit.timeit(get_prices_with_loop, number=100)
    print(f"{with_loop:>.5f} seconds (for loop)")

    # Comparing run times for calculating sales tax on 100,000 items...
    # 1.17696 seconds (map())
    # 1.36382 seconds (list comprehension)
    # 1.59123 seconds (for loop)
