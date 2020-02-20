#! /usr/bin/env python3.7

count = 25


def func(param1=123, param2="hi mom!"):
    count = 37
    print(" locals ".center(20, "*"))
    for k, v in locals().items():
        print(f"key {k}: object {str(v)}")

    print()
    print(" globals ".center(20, "*"))
    for k, v in globals().items():
        print(f"key {k}: object {str(v)}")

    print()
    print(" built-ins ".center(20, "*"))
    print(dir(__builtins__))


func()
