#! /usr/bin/env python3.7
"""Convert Code Listing 1.4 to work outside of the Python REPL."""

import turtle

win = turtle.Screen()
win.setup(400, 400)

tommy = turtle.Turtle()
tommy.speed(1)

tommy.forward(100)
tommy.right(144)
tommy.forward(100)
tommy.right(144)
tommy.forward(100)
tommy.right(144)
tommy.forward(100)
tommy.right(144)
tommy.forward(100)

tommy.hideturtle()

win.mainloop()
