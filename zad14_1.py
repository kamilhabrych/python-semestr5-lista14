from graphics import *
import time

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 1', max_width, max_height)
win.setBackground('white')

oval = Oval(Point(140,100), Point(220,260))
oval.setFill('green')
oval.draw(win)

circle = Circle(Point(20,180), 40)
circle.setFill('red')
circle.draw(win)

rectangle = Rectangle(Point(270,150), Point(370,210))
rectangle.setFill('yellow')
rectangle.draw(win)

pt_rectangle = rectangle.getP1()
pt_oval = oval.getP2()
radius_circle = circle.getRadius()

for move in range(50):
    center_circle = circle.getCenter()
    circle.move(5, 0)
    if center_circle.x-radius_circle < pt_oval.x and center_circle.x+radius_circle > pt_rectangle.x: 
        break
    time.sleep(0.1)

win.getMouse()
win.close()