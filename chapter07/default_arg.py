#! /usr/bin/env python3.7


def append_to(value, to=[]):
    to.append(value)
    return to


my_list = append_to(37)
print(my_list)


my_other_list = append_to(42)
print(my_other_list)
print(my_list)


existing_list = [1, 2, 3, 4]
my_third_list = append_to(12, existing_list)
print(existing_list)
