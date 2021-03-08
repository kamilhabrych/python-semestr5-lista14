from graphics import *
import math
import time
import random

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 5', max_width, max_height)
win.setBackground('white')

circle = Circle(Point(250,250),50)
circle.setFill('brown')
circle.draw(win)
length = 20
alfa = 0
r_circle = circle.getRadius()

while True:
    pt_circle = circle.getCenter() 
    x = math.cos(alfa * math.pi / 180) * length
    y = math.sin(alfa * math.pi / 180) * length

    if pt_circle.x-r_circle + x < 0: 
        alfa = 0
        x = math.cos(alfa * math.pi / 180) * length
        y = math.sin(alfa * math.pi / 180) * length
    elif pt_circle.x + r_circle+x > max_width: 
        alfa = 180
        x = math.cos(alfa * math.pi / 180) * length
        y = math.sin(alfa * math.pi / 180) * length
    elif pt_circle.y - r_circle+y < 0: 
        alfa = 90
        x = math.cos(alfa * math.pi / 180) * length
        y = math.sin(alfa * math.pi / 180) * length
    elif pt_circle.y + r_circle + y > max_height: 
        alfa = 270
        x = math.cos(alfa * math.pi / 180) * length
        y = math.sin(alfa * math.pi / 180) * length

    circle.move(x,y)
    opt = random.randint(1,2)
    if opt == 1: 
        alfa += random.randint(5,20)
    else: 
        alfa -= random.randint(5,20)
    time.sleep(0.1)

win.close()