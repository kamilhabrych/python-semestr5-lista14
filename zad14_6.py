from graphics import *
import math
import time
import random

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 6', max_width, max_height)
win.setBackground('white')

circle = Circle(Point(250,250),50)
circle.setFill('brown')

length = 15
circle.draw(win)
pt_circle = circle.getCenter()
r_circle = circle.getRadius()
circle2 = Circle(Point(pt_circle.x + 85, pt_circle.y),10)
circle2.setFill('black')
circle2.draw(win)
alfa = 90

while True:
    pt_circle2 = circle2.getCenter()
    x = math.cos(alfa * math.pi / 180) * length
    y = math.sin(alfa * math.pi / 180) * length
    circle2.move(x,y)
    alfa += 10
    time.sleep(0.05)

win.close()