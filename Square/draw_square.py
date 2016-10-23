import turtle

def open_window():
    window = turtle.Screen()
    window.bgcolor("red")
    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angel = turtle.Turtle()
    angel.color("green")
    angel.circle(100)

open_window()
draw_square()
draw_circle()
                   
