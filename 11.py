import turtle

screen = turtle.Screen()
screen.title("Turtle Pattern Generator")
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")


def spiral():
    for i in range(100):
        pen.forward(i * 2)
        pen.right(91)


def koch(length, depth):
    if depth == 0:
        pen.forward(length)
    else:
        koch(length / 3, depth - 1)
        pen.left(60)
        koch(length / 3, depth - 1)
        pen.right(120)
        koch(length / 3, depth - 1)
        pen.left(60)
        koch(length / 3, depth - 1)


def snowflake(length, depth):
    for _ in range(3):
        koch(length, depth)
        pen.right(120)


choice = input("Enter 1 for Spiral or 2 for Koch Snowflake: ")

if choice == "1":
    spiral()
elif choice == "2":
    pen.penup()
    pen.goto(-150, 100)
    pen.pendown()
    snowflake(300, 3)
else:
    print("Invalid choice.")

turtle.done()