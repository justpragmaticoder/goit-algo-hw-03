import turtle
import re
from turtle import Terminator
from _tkinter import TclError


def get_recursion_level():
    while True:
        recursion_level = input("Recursion level: ").strip()

        if not re.match("^[0-9]{1,3}$", recursion_level):
            print("Please, type only number")
        else:
            return int(recursion_level)


def draw_snowflake(turtle, recursion_level, size):
    if recursion_level == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_snowflake(turtle, recursion_level - 1, size / 3)
            turtle.left(angle)


def main():
    try:
        recursion_level = get_recursion_level()

        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.title("Koch Snowflake")

        fractal_turtle = turtle.Turtle()
        fractal_turtle.speed(0)

        for _ in range(3):
            draw_snowflake(fractal_turtle, recursion_level, 300)
            fractal_turtle.right(120)

        screen.exitonclick()
        screen.mainloop()
    except (KeyboardInterrupt, Terminator, TclError):
        print("\nInterrupted by user.")
    except Exception as e:
        print(f"\nNon-expected error occured: ${str(e)}")


if __name__ == "__main__":
    main()
