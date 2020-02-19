#! /usr/bin/env python3.8


def add(param_1: float, param_2: float) -> float:
    """Return the sum of two floating point numbers."""
    return param_1 + param_2


int_1: int = 1
int_2: int = 2

add(int_1, int_2)


float_1: float = 2.3
float_2: float = 4.5

add(float_1, float_2)


str_1: str = "Hello "
str_2: str = "world!"

add(str_1, str_2)
