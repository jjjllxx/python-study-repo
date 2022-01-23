"""
File: draw.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-02-05 16:44:42
Function:


"""
import turtle
turtle.color('red', 'yellow')
turtle.speed(10)
turtle.begin_fill()
for i in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
turtle.done()
