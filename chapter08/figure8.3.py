#! /usr/bin/env python3.8


def my_function(formal_parameter):
    print(f"before modification formal_parameters's value is {formal_parameter}")
    formal_parameter[0] = 100
    print(f"after modification formal_parameters's value is {formal_parameter}")


actual_parameter = [1, 2, 3]
my_function(actual_parameter)
print(f"after calling my_function, actual_parameters's value is {actual_parameter}")
