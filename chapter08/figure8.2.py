#! /usr/bin/env python3.8


def my_function(formal_parameter):
    formal_parameter = 32
    print(f"formal_parameters's value is {formal_parameter}, and its id is {id(formal_parameter)}")


actual_parameter = 25
print(f"actual_parameters's id is {id(actual_parameter)}")
my_function(actual_parameter)
