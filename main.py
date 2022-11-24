import turtle
import random


def tree(branch_len, angle, t):
    if branch_len > 0.5:  # base case
        # for a tree with random angles, closer to what you see in nature:
        # angle = random.randint(15, 60)
        t.forward(branch_len)
        t.right(angle)
        tree(branch_len - 10, angle, t)
        t.left(angle * 2)
        tree(branch_len - 10, angle, t)
        t.right(angle)
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("black")
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color("pink")
    angle = random.randint(15, 45)
    tree(80, angle, t)
    window.exitonclick()


main()
