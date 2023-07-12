
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     random_color = (r, g, b)
#     rgb_colors.append(random_color)
#
# print(rgb_colors)

import turtle as t
from random import choice
rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tom = t.Turtle()
my_screen = t.Screen()

t.colormode(255)
tom.speed("fastest")
tom.hideturtle()

tom.setheading(225)
tom.penup()
tom.forward(250)
tom.setheading(0)

for row in range(10):
    for _ in range(10):
        tom.dot(20, choice(rgb_colors))
        tom.penup()
        tom.forward(50)
        tom.pendown()
    tom.penup()
    tom.setheading(90)
    tom.forward(50)
    tom.setheading(180)
    tom.forward(500)
    tom.setheading(0)

my_screen.exitonclick()
