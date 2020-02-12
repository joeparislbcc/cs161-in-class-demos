#! /usr/bin/env python3.7


def append_to(element, to=[]):
    """A seemingly simple function that has often unexpected results."""
    to.append(element)
    return to


# def append_to(element, to=None):
#     """A version of append_to that works as expected."""
#     if to is None:
#         to = []
#     to.append(element)
#     return to


if __name__ == "__main__":
    my_list = append_to(37)
    print(my_list)

    my_other_list = append_to(42)
    print(my_other_list)
