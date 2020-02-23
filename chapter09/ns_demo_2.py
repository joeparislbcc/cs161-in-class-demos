#! /usr/bin/env python3.7
"""This program demonstrates local, enclosing, global, and built-in namespace"""

# this is the global namespace; identifiers delcared here can be seen everywhere
# in the program or script
GLOBAL_VARIABLE = "I AM A GLOBAL VARIABLE"


def outer(outer_param="outer_param"):
    # outer() has access to all identifiers defined in itself, in the global
    # namespace, and in the built-in namespace.

    outer_variable = "outer_variable"

    def inner(inner_param="inner_param"):
        # inner() has access to all identifiers defined in itself, in outer(),
        # in the global namespace, and in the built-in namespace.

        inner_variable = "inner_variable"

        print(f"in function inner(), GLOBAL_VARIABLE = '{GLOBAL_VARIABLE}'")
        print(f"in function inner(), inner_param = '{inner_param}'")
        print(f"in function inner(), inner_variable = '{inner_variable}'")

        print(f"in function inner(), outer_param = '{outer_param}'")
        print(f"in function inner(), outer_variable = '{outer_variable}'")

    print(f"in function outer(), GLOBAL_VARIABLE = '{GLOBAL_VARIABLE}'")
    print(f"in function outer(), outer_param = '{outer_param}'")
    print(f"in function outer(), outer_variable = '{outer_variable}'")

    input()
    print()
    inner()

    input()
    print()
    try:
        print(f"in function outer(), inner_param = '{inner_param}'")
    except NameError:
        print(f"in function outer(), inner_param is not visible")

    try:
        print(f"in function outer(), inner_variable = '{inner_variable}'")
    except NameError:
        print(f"in function outer(), inner_variable is not visible")

    input()
    print()
    print("Hint: remember the print() function is a built-in!")


outer()
