from graphics import *

max_width = 500
max_height = 500

win = GraphWin('Kamil Habrych zadanie 2', max_width, max_height)
win.setBackground('white')

circle = Circle(Point(250,250),50)
circle.setFill('brown')
circle.draw(win)

lengthOfMove = 20

while True:

    pt_circle = circle.getCenter()
    r_circle = circle.getRadius()

    key = win.getKey()

    if key == 'w' and pt_circle.y - r_circle > 0: 
        circle.move(0,-lengthOfMove)
    elif key == 's' and pt_circle.y + r_circle < max_height: 
        circle.move(0,lengthOfMove)
    elif key == 'a' and pt_circle.x - r_circle > 0: 
        circle.move(-lengthOfMove,0)
    elif key == 'd' and pt_circle.x + r_circle < max_width: 
        circle.move(lengthOfMove,0)
    elif key == 'q': 
        break
win.close()