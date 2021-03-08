from graphics import *
import math
import time
import random

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 4', max_width, max_height)
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
    circle.move(x,y)
    opt = random.randint(1,2)
    if opt == 1: 
        alfa += random.randint(5,20)
    else: 
        alfa -= random.randint(5,20)
    time.sleep(0.1)

win.close()