import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black") 
screen.setworldcoordinates(-2, -2, 2, 2)  
t = turtle.Turtle()
t.speed(10)


def draw_function(func, start_x, end_x, step=0.01):
    t.penup()
    x = start_x
    while x <= end_x:
        try:
            y = func(x)
            t.goto(x, y)
            t.pendown()
        except ValueError:
            pass
        x += step
    t.penup()


def draw_filled_ellipse(x_center, y_center, a, b, fill_color="white"):
    t.penup()
    t.color(fill_color)
    t.goto(x_center + a, y_center)
    t.pendown()
    t.begin_fill()  
    for angle in range(361):
        theta = math.radians(angle)
        x = a * math.cos(theta) + x_center
        y = b * math.sin(theta) + y_center
        t.goto(x, y)
    t.end_fill()  #
    t.penup()


def draw_filled_circle(x_center, y_center, radius, fill_color="white"):
    t.penup()
    t.color(fill_color)
    t.goto(x_center + radius, y_center)
    t.pendown()
    t.begin_fill()  
    for angle in range(361):
        theta = math.radians(angle)
        x = radius * math.cos(theta) + x_center
        y = radius * math.sin(theta) + y_center
        t.goto(x, y)
    t.end_fill()  
    t.penup()


def cuberoot(x):
    return math.copysign(abs(x) ** (1/3), x)


def draw_filled_function(func, start_x, end_x, fill_color="blue", step=0.01):
    t.penup()
    t.color(fill_color)
    t.begin_fill() 
    x = start_x
    while x <= end_x:
        try:
            y = func(x)
            t.goto(x, y)
            t.pendown()
        except ValueError:
            pass  
        x += step
    
    t.goto(end_x, 0)  
    t.goto(start_x, 0)  
    t.end_fill()  
    t.penup()

#身體
draw_filled_function(lambda x: 2 * cuberoot(1 - x**2), -1, 1, fill_color="gray")

#波浪
draw_filled_function(lambda x: 0.1 * (1 + math.cos(3 * math.pi * x)), -1, 1, fill_color="black")

#左眼白
draw_filled_ellipse(-0.3, 1.25, math.sqrt(0.0225), math.sqrt(0.0625))

#右眼白
draw_filled_ellipse(0.3, 1.25, math.sqrt(0.0225), math.sqrt(0.0625))

#左黑珠
draw_filled_circle(-0.22, 1.25, math.sqrt(0.0036), fill_color="black")

#右黑珠
draw_filled_circle(0.38, 1.25, math.sqrt(0.0036), fill_color="black")

#嘴巴
draw_filled_ellipse(0, 0.6, math.sqrt(0.01), math.sqrt(0.04), fill_color="black")

t.hideturtle()
screen.mainloop()
